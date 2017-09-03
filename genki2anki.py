#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sqlite3
import os
import tempfile
import apkg
from PIL import Image


KANJI_CROP_Y = 100


def main(genki_dir, output_path, filter_kanji):
    cards_iterator = load_genki_vocab(genki_dir)
    create_base_apkg(cards_iterator, genki_dir, output_path, filter_kanji)


def load_genki_vocab(genki_dir):
    connection = sqlite3.connect(
        os.path.join(genki_dir, 'assets', 'vocab_word.sqlite')
    )
    # Enable selecting fields by name
    connection.row_factory = sqlite3.Row
    return connection.execute('select * from WordsTBL2;')


def create_base_apkg(cards, genki_dir, output_path, filter_kanji):
    anki = apkg.Apkg()

    for card in cards:
        create_card(card, anki, genki_dir, filter_kanji)

    anki.export(output_path)
    anki.cleanup()


def create_card(card, anki, genki_dir, filter_kanji):
    img_template = '<img src="%s" />'
    sound_template = '[sound:%s]'
    english = card['ENG_WORD']
    japanese = card['JPN_WORD']
    en_sentence = card['ENG_TEXT']
    kanji_image_name = card['JPN_WORD_IMAGE']
    kanji_image_tag = img_template % kanji_image_name
    kanji_voice_name = card['JPN_WORD_VOICE'] + '.mp3'
    kanji_voice_tag = sound_template % kanji_voice_name
    jp_sentence_image_name = card['JPN_TEXT']
    jp_sentence_tag = img_template % jp_sentence_image_name
    jp_sentence_voice_name = card['JPN_TEXT_VOICE'] + '.mp3'
    jp_sentence_voice_tag = sound_template % jp_sentence_voice_name
    illustration_name = card['ILLUST']
    illustration_tag = ""
    if illustration_name is not None:
        illustration_tag = img_template % illustration_name
    tags = ' genki-%s ' % card['LESSON']
    part = ''
    if card['PARTS']:
        part = card['PARTS'].replace(' ', '-')
    had_kanji = copy_media(genki_dir, anki, kanji_image_name,
               kanji_voice_name, illustration_name,
               jp_sentence_image_name, jp_sentence_voice_name,
               filter_kanji)
    models = list(range(5))
    if not had_kanji:
        kanji_image_tag = ''
        models.remove(2)
    flds = [
        english,
        japanese,
        kanji_image_tag,
        '',
        illustration_tag,
        kanji_voice_tag,
        part,
        jp_sentence_tag,
        en_sentence,
        jp_sentence_voice_tag
    ]

    anki.add_note(flds, tags, models)


def copy_media(genki_dir, anki, kanji, audio, illus, sent, sent_audio,
               filter_kanji):
    kanji_dir = os.path.join(genki_dir, 'assets', 'appimages', 'midashi')
    sent_dir = os.path.join(genki_dir, 'assets', 'appimages', 'reibun')
    audio_dir = os.path.join(genki_dir, 'assets', 'appsounds', 'midashi')
    sent_audio_dir = os.path.join(genki_dir, 'assets', 'appsounds', 'example')
    illus_dir = None
    if illus:
        illus_dir = os.path.join(genki_dir, 'assets', 'appimages', 'illust')

    kanji_img = Image.open(os.path.join(kanji_dir, kanji))
    xsize, ysize = kanji_img.size
    kanji_cropped = kanji_img.crop((0, 0, xsize, KANJI_CROP_Y))
    had_kanji = is_kanji(kanji_img) if filter_kanji else True
    if had_kanji:
        with tempfile.TemporaryFile() as tmpimg:
            kanji_cropped.save(tmpimg, 'png')
            tmpimg.seek(0)
            anki.add_media(tmpimg, kanji)

    with open(os.path.join(audio_dir, audio), 'rb') as f:
        anki.add_media(f)

    with open(os.path.join(sent_audio_dir, sent_audio), 'rb') as f:
        anki.add_media(f)

    if illus_dir:
        with open(os.path.join(illus_dir, illus), 'rb') as f:
            anki.add_media(f)

    with open(os.path.join(sent_dir, sent), 'rb') as f:
        anki.add_media(f)

    return had_kanji


def is_kanji(kanji_img):
    # Check if the area we cropped out has any furigana. If not, the image
    # wasn't kanji.
    xsize, ysize = kanji_img.size
    kanji_removed = kanji_img.crop((0, KANJI_CROP_Y, xsize, ysize))
    previous_pixel = kanji_removed.getpixel((0, 0))
    has_kanji = False
    for x in range(0, xsize):
        for y in range(ysize - KANJI_CROP_Y):
            if kanji_removed.getpixel((x, y)) != previous_pixel:
                has_kanji = True
                break
        if has_kanji:
            break
    return has_kanji


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
    parser.add_argument(
        '--filter-kanji',
        help=('Attempt to filter out kanji images that contain only kana. '
              'Default value is y. See README for more information.'),
        choices=['y', 'n'],
        default='y'
    )
    args = parser.parse_args()
    main(args.genki_dir, args.output_file, args.filter_kanji == 'y')
