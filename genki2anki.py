#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sqlite3
import os
import tempfile
import apkg
from PIL import Image


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
    anki = apkg.Apkg()

    for card in cards:
        create_card(card, anki, genki_dir)

    anki.export(output_path)
    anki.cleanup()


def create_card(card, anki, genki_dir):
    img_template = '<img src="%s" />'
    sound_template = '[sound:%s]'
    english = card['ENG_WORD']
    japanese = card['JPN_WORD']
    kanji_image_name = card['JPN_WORD_IMAGE']
    kanji_image_tag = img_template % kanji_image_name
    kanji_voice_name = card['JPN_WORD_VOICE'] + '.mp3'
    kanji_voice_tag = sound_template % kanji_voice_name
    illustration_name = card['ILLUST']
    illustration_tag = ""
    if illustration_name is not None:
        illustration_tag = img_template % illustration_name
    tags = ' genki-%s ' % card['LESSON']
    if card['PARTS']:
        tags += '%s ' % card['PARTS'].replace(' ', '-')
    flds = [
        english,
        japanese,
        kanji_image_tag,
        illustration_tag,
        kanji_voice_tag,
    ]

    anki.add_note(flds, tags)

    copy_media(genki_dir, anki, kanji_image_name,
               kanji_voice_name, illustration_name)


def copy_media(genki_dir, anki, kanji, audio, illus):
    kanji_dir = os.path.join(genki_dir, 'assets', 'appimages', 'midashi')
    audio_dir = os.path.join(genki_dir, 'assets', 'appsounds', 'midashi')
    illus_dir = None
    if illus:
        illus_dir = os.path.join(genki_dir, 'assets', 'appimages', 'illust')

    kanji_img = Image.open(os.path.join(kanji_dir, kanji))
    kanji_cropped = kanji_img.crop((0, 0, 539, 100))
    with tempfile.TemporaryFile() as tmpimg:
        kanji_cropped.save(tmpimg, 'png')
        tmpimg.seek(0)
        anki.add_media(tmpimg, kanji)

    with open(os.path.join(audio_dir, audio), 'rb') as f:
        anki.add_media(f)

    if illus_dir:
        with open(os.path.join(illus_dir, illus), 'rb') as f:
            anki.add_media(f)


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
