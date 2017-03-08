#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sqlite3
import os
import sys
import re
import time
import shutil
import json
import zipfile
import ankiutils
from PIL import Image


# TODO: don't hardcode this
MODEL_ID = 1342696646292
DECK_ID = 1488864261175
EPOCH = int(time.time())
reMedia = re.compile("(?i)<img[^>]+src=[\"']?([^\"'>]+)[\"']?[^>]*>")

dedupe = set()


def main(genki_dir, output_path):
    cards_iterator = load_genki_vocab(genki_dir)
    create_base_apkg(cards_iterator, genki_dir, output_path)


def load_genki_vocab(genki_dir):
    connection = sqlite3.connect(
        os.path.join(genki_dir, 'assets', 'vocab_word.sqlite')
    )
    # Enable selecting fields by name
    connection.row_factory = sqlite3.Row
    return connection.execute('select * from WordsTBL2;')


def create_base_apkg(cards, genki_dir, output_path):
    assets_dir = os.path.dirname(os.path.realpath(__file__))
    anki_base = open(os.path.join(assets_dir, 'anki.sql')).read()

    apkg_path = 'genki_apkg'
    if os.path.isfile(apkg_path):
        print('%s exists and is not a directory' % apkg_path)
        sys.exit(1)
    if not os.path.exists(apkg_path):
        os.mkdir(apkg_path)
    if len(os.listdir(apkg_path)) > 0:
        print('%s exists but is not empty' % apkg_path)
        sys.exit(1)

    connection = sqlite3.connect(
        os.path.join(apkg_path, 'collection.anki2')
    )
    connection.executescript(anki_base)
    connection.commit()

    media = []
    i = 0
    for card in cards:
        create_card(card, connection, genki_dir, apkg_path, media)
        i += 1

    connection.close()
    media_file = open(os.path.join(apkg_path, 'media'), 'w')
    json.dump(
        {str(n): media[n] for n in range(len(media))},
        media_file, sort_keys=True
    )
    media_file.close()
    create_zip(apkg_path, output_path)
    shutil.rmtree(apkg_path)


def create_card(card, anki_conn, genki_dir, apkg_path, media):
    ts_id = ankiutils.timestampID(anki_conn, 'notes')
    guid = ankiutils.guid64()
    english = card['ENG_WORD']
    japanese = card['JPN_WORD']
    kanji_image_name = card['JPN_WORD_IMAGE']
    kanji_voice_name = card['JPN_WORD_VOICE'] + '.mp3'
    illustration_name = card['ILLUST']
    illustration_tag = ""
    if illustration_name is not None:
        illustration_tag = '<img src="%s" />' % illustration_name
    tags = ' genki-%s ' % card['LESSON']
    if card['PARTS']:
        tags += '%s ' % card['PARTS'].replace(' ', '-')
    flds = (
        '%s%s<img src="%s" />%s[sound:%s]' %
        (english, japanese, kanji_image_name,
         illustration_tag, kanji_voice_name)
    )
    if flds in dedupe:
        print('DUPE: %s' % english)
        return
    dedupe.add(flds)
    print(english)

    copy_media(genki_dir, apkg_path, media, kanji_image_name,
               kanji_voice_name, illustration_name)

    anki_conn.execute(
        """INSERT INTO "notes" VALUES(:tsid,:guid,:mid,:ts,-1,:tags,:flds,:front,:csum,0,'');""",
        {
            'tsid': ts_id,
            'guid': guid,
            'mid': MODEL_ID,
            'ts': EPOCH,
            'tags': tags,
            'flds': flds,
            'front': english,
            'csum': ankiutils.fieldChecksum(english)
        }
    )

    cards_tsid = ankiutils.timestampID(anki_conn, 'cards')
    anki_conn.execute(
        """INSERT INTO "cards" VALUES(:tsid,:nid,:did,0,:mod,0,0,0,76,0,0,0,0,0,0,0,0,'');""",
        {
            'tsid': cards_tsid,
            'nid': ts_id,
            'did': DECK_ID,
            'mod': MODEL_ID,
        }
    )
    anki_conn.execute(
        """INSERT INTO "cards" VALUES(:tsid,:nid,:did,1,:mod,0,0,0,76,0,0,0,0,0,0,0,0,'');""",
        {
            'tsid': cards_tsid + 1,
            'nid': ts_id,
            'did': DECK_ID,
            'mod': MODEL_ID,
        }
    )
    anki_conn.commit()


def copy_media(genki_dir, output_dir, media, kanji, audio, illus):
    kanji_dir = os.path.join(genki_dir, 'assets', 'appimages', 'midashi')
    audio_dir = os.path.join(genki_dir, 'assets', 'appsounds', 'midashi')
    illus_dir = None
    if illus:
        illus_dir = os.path.join(genki_dir, 'assets', 'appimages', 'illust')

    media.append(kanji)
    kanji_img = Image.open(os.path.join(kanji_dir, kanji))
    kanji_cropped = kanji_img.crop((0, 0, 539, 100))
    kanji_cropped.save(os.path.join(output_dir, str(len(media) - 1)), 'png')

    media.append(audio)
    shutil.copy(
        os.path.join(audio_dir, audio),
        os.path.join(output_dir, str(len(media) - 1))
    )

    if illus_dir:
        media.append(illus)
        shutil.copy(
            os.path.join(illus_dir, illus),
            os.path.join(output_dir, str(len(media) - 1))
        )


def create_zip(indir, outfile):
    zf = zipfile.ZipFile(outfile, 'w', zipfile.ZIP_DEFLATED)
    for f in os.listdir(indir):
        zf.write(os.path.join(indir, f), arcname=f)
    zf.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'genki_dir',
        help='Path to the extracted GENKI Vocab apk contents.'
    )
    parser.add_argument(
        'output_file',
        help=('Desired path to output apkg file.'
              ' THIS WILL BE OVERWRITTEN IF IT EXISTS!')
    )
    args = parser.parse_args()
    main(args.genki_dir, args.output_file)
