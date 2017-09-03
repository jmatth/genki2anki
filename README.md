```
usage: genki2anki.py [-h] [--filter-kanji {y,n}] genki_dir output_file

positional arguments:
  genki_dir             Path to the extracted GENKI Vocab apk contents.
  output_file           Desired path to output apkg file. THIS WILL BE
                        OVERWRITTEN IF IT EXISTS!

optional arguments:
  -h, --help            show this help message and exit
  --filter-kanji {y,n}  Attempt to filter out kanji images that contain only
                        kana. Default value is y. See README for more
                        information.
```


# genki2anki
This is a script to convert the assets from the
[GENKI Vocab Cards](https://play.google.com/store/apps/details?id=jp.co.japantimes.genkivocab)
Android app into a deck for the [Anki flashcard software](https://apps.ankiweb.net/).
The assets themselves are not included in this repo.
You will have to buy the application and extract them yourself.

The resulting notes will have each word in English, Japanese in Kana, Japanese
in Kanji (as an image), the reading audio, and the illustration if one exists.
It will also tag each card with its Genki lesson (chapter).


## Step By Step Instructions
Prerequisites: python3 with pip
1. Clone this repo and install the dependencies with `pip3 install -r requirements.txt`
2. [Install adb](https://developer.android.com/studio/index.html#downloads) on
   your computer and
   [enable USB debugging](https://www.howtogeek.com/129728/how-to-access-the-developer-options-menu-and-enable-usb-debugging-on-android-4.2/)
   on your Android device.
3. Purchase the [Genki Vocab App](http://example.com) from the Play Store and
   install it on your device.
4. Determine where the apk is stored on your device with the command `adb shell
   pm path jp.co.japantimes.genkivocab`. This should produce output that looks
   like `package:<PATH_TO_APK>`. Copy everything after the colon.
5. Copy the apk to your computer with the command `adb pull <PATH_TO_APK>`,
   where `<PATH_TO_APK>` is the path from the previous step.
6. Unzip the apk. Depending on how you do this you might need to change the
   extension from `.apk` to `.zip`.
7. Run this program with the path to the extracted apk contents as the first
   argument and the desired output file as the second: `./genki2anki.py
   /path/to/genki ./anki.apkg`.

If everything goes well you should see a long list of words scroll down the
screen and the file you specified will be created. You can then import it into
Anki.


## Options
`--filter-kanji`: Kanji in the Genki app are stored as plain png images that
include both the Kanji and furigana. Unfortunately some words don't have kanji
associated with them so the included image just contains kana, resulting in anki
cards that are duplicates (we already have cards for the kana alone). If this
flag is turned on (it is on by default) then the script will try to check for
the presence of furigana in each kanji image, and exclude any where it is not
found. This effectively filters out the 375 images that contain kana instead of
kanji, but does slow down deck generation a bit and could break if a significant
app update changes how the images are laid out. I recommend leaving it turned on
unless your generated deck turns out to be missing a bunch of kanji cards (also
if that happens, please file a bug so I can fix it).


## FAQ
## What's this empty "UKanji" field in the notes?
This is in case you want to add unicode versions of the Kanji to replace the
images from the Genki app. The cards are written to show the UKanji field if it
is not empty, the Kanji field otherwise, and not generate the card at all if
both are empty. Also, if you do fill in the UKanji field you can toggle between
the two fields by tapping or clicking on the kanji on the cards. Personally I've
used this feature to change some of the kanji (友だち to 友達), add some extra
cards from Tae Kim's grammar guide in a way that doesn't stand out from the rest
of the cards, and just to have more recognizable unicode characters instead of
stylized calligraphy while reviewing. Feel free to ignore or even delete this
field if it doesn't sound useful to you.

### I don't like the card layout, how can I change it?
While it's possible to hack the python script to change how the deck is
generated, it's probably not worth the effort right now since a lot of it exists
in json embedded in sql queries and a handful of unique ids are hardcoded. A far
easier option is to just generate the deck and then customize the notes and
cards inside of Anki. You can find extensive documentation on how to do so on
Anki's own website
[here](https://apps.ankiweb.net/docs/manual.html#cards-and-templates).  Maybe
one day I'll break out the templates into their own HTML files for easier
customization, but probably not.

### I don't want sentences (or kanji or whatever) as separate cards.
If you don't like having certain cards then you should delete the card type
after importing the cards into Anki. For reasons discussed in the previous
question, it is not practical to support generating decks with some cards
included or excluded, so instead the script tries to include every possible card
with every piece of information from the Genki app so you can customize it
however you'd like. For example, I removed the sentence card types but moved the
example sentences to the backs of other cards so I could still use them for
practice.


## Known Issues
* Some of the readings have hints in parenthesis that give away the English
  meaning (for example "あの (um . . .)"). Your best option is just do edit the
  cards as they come up during study sessions.
