```
usage: genki2anki.py [-h] genki_dir output_file

positional arguments:
  genki_dir    Path to the extracted GENKI Vocab apk contents.
  output_file  Desired path to output apkg file. THIS WILL BE OVERWRITTEN IF
               IT EXISTS!

optional arguments:
  -h, --help   show this help message and exit
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
1. [Install adb](https://developer.android.com/studio/index.html#downloads) on
   your computer and
   [enable USB debugging](https://www.howtogeek.com/129728/how-to-access-the-developer-options-menu-and-enable-usb-debugging-on-android-4.2/)
   on your Android device.
2. Purchase the [Genki Vocab App](http://example.com) from the Play Store and
   install it on your device.
3. Determine where the apk is stored on your device with the command `adb shell
   pm path jp.co.japantimes.genkivocab`. This should produce output that looks
   like `package:<PATH_TO_APK>`. Copy everything after the colon.
4. Copy the apk to your computer with the command `adb pull <PATH_TO_APK>`,
   where `<PATH_TO_APK>` is the path from the previous step.
5. Unzip the apk. Depending on how you do this you might need to change the
   extension from `.apk` to `.zip`.
6. Run this program with the path to the extracted apk contents as the first
   argument and the desired output file as the second: `./genki2anki.py
   /path/to/genki ./anki.apkg`.

If everything goes well you should see a long list of words scroll down the
screen and the file you specified will be created. You can then import it into
Anki.


## Customizing The Deck
While it's possible to hack the python script to change how the deck is
generated, it's probably not worth the effort right now since a lot of it exists
in json embedded in sql queries and a handful of unique ids are hardcoded. A far
easier option is to just generate the deck and then customize the notes and
cards inside of Anki. Maybe one day I'll break out the templates into their own
HTML files for easier customization, but probably not.


## Known Issues
* Some cards will be created where the "kanji" image is just a duplicate of the
  kana reading. This is a result of how Genki structured the data within their
  app and can't be helped. The simplest solution is to just edit such cards as
  they come up during your study sessions and delete the image from the kanji
  field. Then once you're done click `Tools -> Empty Cards...` to have Anki
  remove the now empty kanji cards. Since most cards don't have kanji until
  lesson 3, it might also be preferable to go through notes from the first two
  lessons and modify each card to remove the kanji before you start using the
  deck.
* Some of the readings have hints in parenthesis that give away the English
  meaning (for example "あの (um . . .)"). Your best option is just do edit the
  cards as they come up during study sessions.
