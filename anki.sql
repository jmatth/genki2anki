PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE col (
    id              integer primary key,
    crt             integer not null,
    mod             integer not null,
    scm             integer not null,
    ver             integer not null,
    dty             integer not null,
    usn             integer not null,
    ls              integer not null,
    conf            text not null,
    models          text not null,
    decks           text not null,
    dconf           text not null,
    tags            text not null
);
INSERT INTO "col" VALUES(1,1500451200,1500556111928,1500556111925,11,0,0,0,'{"nextPos": 1, "estTimes": true, "activeDecks": [1], "sortType": "noteFld", "timeLim": 0, "sortBackwards": false, "addToCur": true, "curDeck": 1, "newBury": true, "newSpread": 0, "dueCounts": true, "curModel": "1500556111925", "collapseTime": 1200}','{"1342696646293": {"vers": [], "name": "Japanese-85136", "tags": [], "did": 1488864261175, "usn": -1, "req": [[1, "any", [1, 5, 6]], [0, "any", [0, 4, 6]], [2, "any", [2, 3]], [3, "any", [7, 9]], [4, "all", [8]]], "flds": [{"name": "English", "media": [], "sticky": false, "rtl": false, "ord": 0, "font": "Arial", "size": 12}, {"name": "Japanese", "media": [], "sticky": false, "rtl": false, "ord": 1, "font": "Arial", "size": 12}, {"name": "Kanji", "media": [], "sticky": false, "rtl": false, "ord": 2, "font": "Arial", "size": 20}, {"size": 20, "name": "UKanji", "media": [], "rtl": false, "ord": 3, "font": "Arial", "sticky": false}, {"name": "Picture", "media": [], "sticky": false, "rtl": false, "ord": 4, "font": "Arial", "size": 20}, {"name": "Audio", "media": [], "sticky": false, "rtl": false, "ord": 5, "font": "Arial", "size": 20}, {"size": 20, "name": "Part", "media": [], "rtl": false, "ord": 6, "font": "Arial", "sticky": false}, {"name": "JpSentence", "media": [], "sticky": false, "rtl": false, "ord": 7, "font": "Arial", "size": 20}, {"name": "EnSentence", "media": [], "sticky": false, "rtl": false, "ord": 8, "font": "Arial", "size": 20}, {"name": "SentenceAudio", "media": [], "sticky": false, "rtl": false, "ord": 9, "font": "Arial", "size": 20}], "sortf": 0, "tmpls": [{"name": "Reading", "qfmt": "<div class=\"part part-{{Part}}\" ></div>\n<div class=\"meaning\">{{English}}</div>\n{{#Picture}}\n<div class=\"illustration\">{{Picture}}</div>\n{{/Picture}}", "did": null, "bafmt": "", "afmt": "<div class=\"back\">\n{{FrontSide}}\n</div>\n\n<hr id=\"answer\" />\n\n{{#Kanji}}\n\t<div id=\"kanji\" class=\"kanji\" {{#UKanji}}style=\"display:none;\" onclick=\"toggleUKanji();\"{{/UKanji}}>{{Kanji}}</div>\n{{/Kanji}}\n\n{{#UKanji}}\n<div id=\"ukanji\" class=\"kanji\" onclick=\"toggleKanji();\">{{UKanji}}</div>\n\n<script type=\"text/javascript\">\nfunction toggleKanji() {\n\tdocument.getElementById(\"ukanji\").style.display = \"none\";\n\tdocument.getElementById(\"kanji\").style.removeProperty(\"display\");\n}\n\nfunction toggleUKanji() {\n\tdocument.getElementById(\"kanji\").style.display = \"none\";\n\tdocument.getElementById(\"ukanji\").style.removeProperty(\"display\");\n}\n</script>\n{{/UKanji}}\n\n<div class=\"reading\">{{Japanese}}</div>\n\n<div class=\"audio\">{{Audio}}</div>\n\n{{#Expression}}\n<br />\n<div class=\"jpSentence\">{{furigana:Reading}}</div>\n<div class=\"jpSentenceAudio\">{{JapaneseSentenceAudio}}</div>\n<div class=\"englishSentence\">{{hint:EnglishSentence}}</div>\n{{/Expression}}", "ord": 1, "bqfmt": ""}, {"name": "English", "qfmt": "<div class=\"part part-{{Part}}\" ></div>\n\n<div class=\"reading\">{{Japanese}}</div>\n\n<div class=\"audio\">{{Audio}}</div>", "did": null, "bafmt": "", "afmt": "<div class=\"back\">\n{{FrontSide}}\n</div>\n\n<hr id=answer>\n\n{{#Kanji}}\n\t<div id=\"kanji\" class=\"kanji\" {{#UKanji}}style=\"display:none;\" onclick=\"toggleUKanji();\"{{/UKanji}}>{{Kanji}}</div>\n{{/Kanji}}\n\n{{#UKanji}}\n<div id=\"ukanji\" class=\"kanji\" onclick=\"toggleKanji();\">{{UKanji}}</div>\n\n<script type=\"text/javascript\">\nfunction toggleKanji() {\n\tdocument.getElementById(\"ukanji\").style.display = \"none\";\n\tdocument.getElementById(\"kanji\").style.removeProperty(\"display\");\n}\n\nfunction toggleUKanji() {\n\tdocument.getElementById(\"kanji\").style.display = \"none\";\n\tdocument.getElementById(\"ukanji\").style.removeProperty(\"display\");\n}\n</script>\n{{/UKanji}}\n\n<div class=\"meaning\">{{English}}</div>\n\n{{#Picture}}\n<div class=\"illustration\">{{Picture}}</div>\n{{/Picture}}", "ord": 0, "bqfmt": ""}, {"name": "Kanji", "qfmt": "{{#Kanji}}{{^UKanji}}\n\t<div style=\"margin-bottom:15px\" class=\"part part-{{Part}}\" ></div>\n{{/UKanji}}{{/Kanji}}\n{{#UKanji}}\n\t<div style=\"margin-bottom:15px\" class=\"part part-{{Part}}\" ></div>\n{{/UKanji}}\n\n{{#Kanji}}\n\t<div id=\"kanji\" class=\"kanji\" {{#UKanji}}style=\"display:none;\" onclick=\"toggleUKanji();\"{{/UKanji}}>{{Kanji}}</div>\n{{/Kanji}}\n\n{{#UKanji}}\n<div id=\"ukanji\" class=\"kanji\" onclick=\"toggleKanji();\">{{UKanji}}</div>\n\n<script type=\"text/javascript\">\nfunction toggleKanji() {\n\tdocument.getElementById(\"ukanji\").style.display = \"none\";\n\tdocument.getElementById(\"kanji\").style.removeProperty(\"display\");\n}\n\nfunction toggleUKanji() {\n\tdocument.getElementById(\"kanji\").style.display = \"none\";\n\tdocument.getElementById(\"ukanji\").style.removeProperty(\"display\");\n}\n</script>\n{{/UKanji}}", "did": null, "bafmt": "", "afmt": "<div class=\"back\">\n{{FrontSide}}\n</div>\n\n<hr id=answer>\n\n<span class=\"reading\">{{Japanese}}</span>\n\n<div class=\"audio\">{{Audio}}</div>\n\n<span class=\"meaning\">{{English}}</span>\n\n{{#Picture}}\n<div class=\"illustration\">{{Picture}}</div>\n{{/Picture}}\n\n{{#Expression}}\n<br />\n<br />\n<div class=\"jpSentence\">{{furigana:Reading}}</div>\n<div class=\"jpSentenceAudio\">{{JapaneseSentenceAudio}}</div>\n<div class=\"englishSentence\">{{hint:EnglishSentence}}</div>\n{{/Expression}}", "ord": 2, "bqfmt": ""}, {"name": "JpSentence", "qfmt": "{{#JpSentence}}\n<span id=\"jpsentence\">{{JpSentence}}</span>\n{{/JpSentence}}\n\n<div id=\"audio\">{{SentenceAudio}}</div>", "did": null, "bafmt": "", "afmt": "{{FrontSide}}\n\n<hr id=answer><span id=\"ensentence\">{{EnSentence}}</span>", "ord": 3, "bqfmt": ""}, {"name": "EnSentence", "qfmt": "<span id=\"ensentence\">{{EnSentence}}</span>", "did": null, "bafmt": "", "afmt": "{{FrontSide}}\n\n<hr id=answer>{{#JpSentence}}\n<span id=\"jpsentence\">{{JpSentence}}</span>\n{{/JpSentence}}\n\n<div id=\"audio\">{{SentenceAudio}}</div>", "ord": 4, "bqfmt": ""}], "mod": 1500556063, "latexPost": "\\end{document}", "type": 0, "id": 1342696646293, "css": ".card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n background-color: white;\n}\n\n.card1 { background-color: #FFFFFF; }\n.card2 { background-color: #FFFFFF; }\n\ndiv {\n margin-bottom: 0px;\n margin-top: 0px;\n}\n\nhr {\n margin-top: 25px;\n}\n\n.audio {\n}\n\n.reading {\n font-size: 40px;\n margin-top: 10px;\n}\n\n.meaning {\n font-size: 32px;\n}\n\n.kanji img {\n max-height: 55px;\n padding-top: 9px;\n margin-bottom: -20px;\n}\n\n.kanji {\n height: 55px;\n margin-top: -10px;\n font-size:40px;\n}\n\n.illustration {\n margin-top: 10px;\n}\n\n.illustration img {\n max-height: 200px;\n}\n\n.back {\n margin-bottom: -15px;\n}\n\n.part {\n color: white;\n background: GainsBoro;\n height: 22px;\n line-height: 20px;\n text-align: right;\n padding-right: 7px;\n margin-bottom: 10px\n}\n\n.back .part-ru-verb {\n background: LimeGreen;\n}\n\n.back .part-ru-verb::after {\n content: ''ru-verb''\n}\n\n.back .part-u-verb {\n background: RosyBrown;\n}\n\n.back .part-u-verb::after {\n content: ''u-verb''\n}\n\n.back .part-irregular-verb {\n background: SteelBlue;\n}\n\n.back .part-irregular-verb::after {\n content: ''irregular verb'';\n}\n\n.back .part-noun {\n background: LightCoral;\n}\n\n.back .part-noun::after {\n content: ''noun'';\n}\n.back .part-\u3044-adjective {\n background: DarkSeaGreen;\n}\n.back .part-\u3044-adjective::after {\n content: ''\u3044-adjective'';\n}\n.back .part-\u306a-adjective {\n background: Thistle;\n}\n.back .part-\u306a-adjective::after {\n content: ''\u306a-adjective'';\n}\n\n.hidekana ruby rt{\n visibility: hidden;\n}\n\nruby:hover rt{\n visibility: visible;\n}", "latexPre": "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n\\usepackage{amssymb,amsmath}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n"}}','{"1": {"desc": "", "name": "Default", "extendRev": 50, "usn": 0, "collapsed": false, "newToday": [0, 0], "timeToday": [0, 0], "dyn": 0, "extendNew": 10, "conf": 1, "revToday": [0, 0], "lrnToday": [0, 0], "id": 1, "mod": 1500556111}, "1500504143100": {"name": "Genki Vocab", "extendRev": 50, "usn": -1, "collapsed": false, "browserCollapsed": true, "newToday": [1, 0], "timeToday": [1, 0], "dyn": 0, "extendNew": 10, "conf": 1, "revToday": [1, 0], "lrnToday": [1, 0], "id": 1500504143100, "mod": 1500504623, "desc": ""}}','{"1": {"name": "Default", "replayq": true, "lapse": {"leechFails": 8, "minInt": 1, "delays": [10], "leechAction": 0, "mult": 0}, "rev": {"perDay": 100, "fuzz": 0.05, "ivlFct": 1, "maxIvl": 36500, "ease4": 1.3, "bury": true, "minSpace": 1}, "timer": 0, "maxTaken": 60, "usn": 0, "new": {"perDay": 20, "delays": [1, 10], "separate": true, "ints": [1, 4, 7], "initialFactor": 2500, "bury": true, "order": 1}, "mod": 0, "id": 1, "autoplay": true}}','{}');
CREATE TABLE notes (
    id              integer primary key,   /* 0 */
    guid            text not null,         /* 1 */
    mid             integer not null,      /* 2 */
    mod             integer not null,      /* 3 */
    usn             integer not null,      /* 4 */
    tags            text not null,         /* 5 */
    flds            text not null,         /* 6 */
    sfld            integer not null,      /* 7 */
    csum            integer not null,      /* 8 */
    flags           integer not null,      /* 9 */
    data            text not null          /* 10 */
);
CREATE TABLE cards (
    id              integer primary key,   /* 0 */
    nid             integer not null,      /* 1 */
    did             integer not null,      /* 2 */
    ord             integer not null,      /* 3 */
    mod             integer not null,      /* 4 */
    usn             integer not null,      /* 5 */
    type            integer not null,      /* 6 */
    queue           integer not null,      /* 7 */
    due             integer not null,      /* 8 */
    ivl             integer not null,      /* 9 */
    factor          integer not null,      /* 10 */
    reps            integer not null,      /* 11 */
    lapses          integer not null,      /* 12 */
    left            integer not null,      /* 13 */
    odue            integer not null,      /* 14 */
    odid            integer not null,      /* 15 */
    flags           integer not null,      /* 16 */
    data            text not null          /* 17 */
);
CREATE TABLE revlog (
    id              integer primary key,
    cid             integer not null,
    usn             integer not null,
    ease            integer not null,
    ivl             integer not null,
    lastIvl         integer not null,
    factor          integer not null,
    time            integer not null,
    type            integer not null
);
CREATE TABLE graves (
    usn             integer not null,
    oid             integer not null,
    type            integer not null
);
ANALYZE sqlite_master;
INSERT INTO "sqlite_stat1" VALUES('col',NULL,'1');
CREATE INDEX ix_notes_usn on notes (usn);
CREATE INDEX ix_cards_usn on cards (usn);
CREATE INDEX ix_revlog_usn on revlog (usn);
CREATE INDEX ix_cards_nid on cards (nid);
CREATE INDEX ix_cards_sched on cards (did, queue, due);
CREATE INDEX ix_revlog_cid on revlog (cid);
CREATE INDEX ix_notes_csum on notes (csum);
COMMIT;
