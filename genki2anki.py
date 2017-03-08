#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sqlite3
import random
import string
import os
import sys
import re
import time
import shutil
import json
import zipfile
from PIL import Image
from hashlib import sha1


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
        print('%s exists and is not a directory')
        sys.exit(1)
    if not os.path.exists(apkg_path):
        os.mkdir(apkg_path)
    if len(os.listdir(apkg_path)) > 0:
        print('%s exists but is not empty')
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
    ts_id = timestampID(anki_conn, 'notes')
    guid = guid64()
    english = card['ENG_WORD']
    japanese = card['JPN_WORD']
    kanji_image_name = card['JPN_WORD_IMAGE']
    kanji_voice_name = card['JPN_WORD_VOICE'] + '.mp3'
    illustration_name = card['ILLUST']
    illustration_tag = ""
    if illustration_name is not None:
        illustration_tag = '<img src="%s" />' % illustration_name
    tags = ' genki-%s ' %  card['LESSON']
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
            'csum': fieldChecksum(english)
        }
    )

    cards_tsid = timestampID(anki_conn, 'cards')
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


#######################################################
#  Helper functions copied from the Anki source code  #
#######################################################

def intTime(scale=1):
    "The time in integer seconds. Pass scale=1000 to get milliseconds."
    return int(time.time()*scale)


def timestampID(db, table):
    "Return a non-conflicting timestamp for table."
    # be careful not to create multiple objects without flushing them, or they
    # may share an ID.
    t = intTime(1000)
    while db.execute("select id from %s where id = ?" % table, (t,)).fetchone() is not None:
        t += 1
    return t


# used in ankiweb
def base62(num, extra=""):
    s = string; table = s.ascii_letters + s.digits + extra
    buf = ""
    while num:
        num, i = divmod(num, len(table))
        buf = table[i] + buf
    return buf


def base91(num):
    _base91_extra_chars = "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
    # all printable characters minus quotes, backslash and separators
    return base62(num, _base91_extra_chars)


def guid64():
    "Return a base91-encoded 64bit random number."
    return base91(random.randint(0, 2**64-1))


reStyle = re.compile("(?si)<style.*?>.*?</style>")
reScript = re.compile("(?si)<script.*?>.*?</script>")
reTag = re.compile("<.*?>")
reEnts = re.compile("&#?\w+;")
reMedia = re.compile("(?i)<img[^>]+src=[\"']?([^\"'>]+)[\"']?[^>]*>")

def entsToTxt(html):
    # entitydefs defines nbsp as \xa0 instead of a standard space, so we
    # replace it first
    html = html.replace("&nbsp;", " ")
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return chr(int(text[3:-1], 16))
                else:
                    return chr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = chr(name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return reEnts.sub(fixup, html)


def stripHTML(s):
    s = reStyle.sub("", s)
    s = reScript.sub("", s)
    s = reTag.sub("", s)
    s = entsToTxt(s)
    return s


def stripHTMLMedia(s):
    "Strip HTML but keep media filenames"
    s = reMedia.sub(" \\1 ", s)
    return stripHTML(s)


def checksum(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    return sha1(data).hexdigest()


def fieldChecksum(data):
    # 32 bit unsigned number from first 8 digits of sha1 hash
    return int(checksum(stripHTMLMedia(data).encode("utf-8"))[:8], 16)


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
