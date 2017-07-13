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
INSERT INTO "col" VALUES(1,1477209600,1489632502829,1489632502616,11,0,0,0,'{"nextPos": 1, "estTimes": true, "activeDecks": [1], "sortType": "noteFld", "timeLim": 0, "sortBackwards": false, "addToCur": true, "curDeck": 1, "newBury": true, "newSpread": 0, "dueCounts": true, "curModel": "1489632502617", "collapseTime": 1200}','{"1342696646293":{"vers":[],"name":"Japanese-85136","tags":[],"did":1488864261175,"usn":42,"req":[[0,"any",[0,3]],[1,"any",[1,4]],[2,"all",[2]]],"flds":[{"name":"Meaning","media":[],"sticky":false,"rtl":false,"ord":0,"font":"Arial","size":12},{"name":"Reading","media":[],"sticky":false,"rtl":false,"ord":1,"font":"Arial","size":12},{"name":"Kanji","media":[],"sticky":false,"rtl":false,"ord":2,"font":"Arial","size":20},{"name":"Picture","media":[],"sticky":false,"rtl":false,"ord":3,"font":"Arial","size":20},{"name":"Audio","media":[],"sticky":false,"rtl":false,"ord":4,"font":"Arial","size":20},{"name":"JpSentence","media":[],"sticky":false,"rtl":false,"ord":5,"font":"Arial","size":20},{"name":"EnSentence","media":[],"sticky":false,"rtl":false,"ord":6,"font":"Arial","size":20},{"name":"SentenceAudio","media":[],"sticky":false,"rtl":false,"ord":7,"font":"Arial","size":20}],"sortf":0,"latexPre":"\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n\\usepackage{amssymb,amsmath}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n","tmpls":[{"name":"Reading","qfmt":"<span style=\"font-size: 50px; \">{{Reading}}</span>\n\n<div id=\"audio\">{{Audio}}</div>","did":null,"bafmt":"","afmt":"{{FrontSide}}\n\n<hr id=answer>\n\n{{#Kanji}}\n<div>{{Kanji}}</div>\n{{/Kanji}}\n\n\n{{#Picture}}\n{{Picture}}\n</br>\n{{/Picture}}\n\n<span style=\"font-size: 50px; \">{{Meaning}}</span>\n\n</br>\n\n<script>\n\tdocument.getElementById(''kanji'').classList.remove(''hidekana'');\n</script>","ord":1,"bqfmt":""},{"name":"English","qfmt":"<span style=\"font-size: 50px; \" id=\"kanji\" class=\"hidekana\">{{Meaning}}</span>\n</br>\n{{#Picture}}\n{{Picture}}\n{{/Picture}}","did":null,"bafmt":"","afmt":"{{FrontSide}}\n\n<hr id=answer>\n\n{{#Kanji}}\n<div style=\"font-size: 50px; \">{{Kanji}}</div>\n{{/Kanji}}\n<div style=\"font-size: 50px; \">{{Reading}}</div>\n\n<div >{{Audio}}</div>","ord":0,"bqfmt":""},{"name":"Kanji","qfmt":"{{#Kanji}}\n<span style=\"font-size: 50px; \" id=\"kanji\" class=\"hidekana\">{{Kanji}}</span>\n{{/Kanji}}","did":null,"bafmt":"","afmt":"<span style=\"font-size: 50px; \" id=\"kanji\" class=\"hidekana\">{{Kanji}}</span>\n\n<hr id=answer>\n\n<span style=\"font-size: 50px; \" id=\"kanji\" class=\"hidekana\">{{Reading}}</span>\n\n<div id=\"audio\">{{Audio}}</div>\n\n\n{{#Picture}}\n{{Picture}}\n</br>\n{{/Picture}}\n\n<span style=\"font-size: 50px; \">{{Meaning}}</span>\n\n</br>\n\n<script>\n\tdocument.getElementById(''kanji'').classList.remove(''hidekana'');\n</script>","ord":2,"bqfmt":""},{"name":"JpSentence","qfmt":"{{#JpSentence}}\n<span id=\"jpsentence\">{{JpSentence}}</span>\n{{/JpSentence}}\n\n<div id=\"audio\">{{SentenceAudio}}</div>","did":null,"bafmt":"","afmt":"{{FrontSide}}\n\n<hr id=answer><span id=\"ensentence\">{{EnSentence}}</span>","ord":3,"bqfmt":""},{"name":"EnSentence","qfmt":"<span id=\"ensentence\">{{EnSentence}}</span>","did":null,"bafmt":"","afmt":"{{FrontSide}}\n\n<hr id=answer>{{#JpSentence}}\n<span id=\"jpsentence\">{{JpSentence}}</span>\n{{/JpSentence}}\n\n<div id=\"audio\">{{SentenceAudio}}</div>","ord":4,"bqfmt":""}],"latexPost":"\\end{document}","type":0,"id":1342696646293,"css":".card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n background-color: white;\n}\n\n.card1 { background-color: #FFFFFF; }\n.card2 { background-color: #FFFFFF; }\n\n.hidekana ruby rt{\n visibility: hidden;\n}\n\nruby:hover rt{\n visibility: visible;\n}","mod":1489588302}}','{"1": {"desc": "", "name": "Default", "extendRev": 50, "usn": 0, "collapsed": false, "newToday": [0, 0], "timeToday": [0, 0], "dyn": 0, "extendNew": 10, "conf": 1, "revToday": [0, 0], "lrnToday": [0, 0], "id": 1, "mod": 1489632502}, "1488984677983": {"name": "Genki Vocab", "extendRev": 50, "usn": 44, "collapsed": false, "browserCollapsed": true, "newToday": [143, 20], "timeToday": [143, 482644], "dyn": 0, "extendNew": 10, "conf": 1, "revToday": [143, 28], "lrnToday": [143, 16], "id": 1488984677983, "mod": 1489617663, "desc": ""}}','{"1": {"name": "Default", "replayq": true, "lapse": {"leechFails": 8, "minInt": 1, "delays": [10], "leechAction": 0, "mult": 0}, "rev": {"perDay": 100, "fuzz": 0.05, "ivlFct": 1, "maxIvl": 36500, "ease4": 1.3, "bury": true, "minSpace": 1}, "timer": 0, "maxTaken": 60, "usn": 0, "new": {"perDay": 20, "delays": [1, 10], "separate": true, "ints": [1, 4, 7], "initialFactor": 2500, "bury": true, "order": 1}, "mod": 0, "id": 1, "autoplay": true}}','{}');
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
