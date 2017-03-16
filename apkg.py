# -*- coding: utf-8 -*-

import tempfile
import sqlite3
import time
import os
import shutil
import json
import zipfile
import ankiutils


# TODO: Don't hardcode this
MODEL_ID = 1342696646293
DECK_ID = 1488984677983


class Apkg(object):

    """A helper class for building Anki apkg archives"""

    def __init__(self):
        self._media = []
        self._dedupe = set()
        self._order = 0
        self._temp_dir = tempfile.TemporaryDirectory(prefix='tmpapkg-')
        self._connection = sqlite3.connect(
            os.path.join(self._temp_dir.name, 'collection.anki2')
        )
        self._initialize_db()

    def _initialize_db(self):
        assets_dir = os.path.dirname(os.path.realpath(__file__))
        anki_base = open(os.path.join(assets_dir, 'nanki.sql')).read()
        self._connection.executescript(anki_base)
        self._connection.commit()

    def _get_next_order(self):
        val = self._order
        self._order += 1
        return val

    def add_note(self, flds_list, tags=""):
        flds = ''.join(flds_list)
        if flds in self._dedupe:
            print('DUPE: %s' % flds_list[0])
            return
        self._dedupe.add(flds)
        print(flds_list[0])
        note_tsid = ankiutils.timestampID(self._connection, 'notes')
        self._connection.execute(
            """\
                INSERT INTO "notes"
                VALUES(:tsid,:guid,:mid,:ts,-1,:tags,:flds,:front,:csum,0,'');
            """,
            {
                'tsid': note_tsid,
                'guid': ankiutils.guid64(),
                'mid': MODEL_ID,
                'ts': int(time.time()),
                'tags': ' %s ' % tags.strip(),
                'flds': flds,
                'front': flds_list[0],
                'csum': ankiutils.fieldChecksum(flds_list[0])
            }
        )

        cards_tsid = ankiutils.timestampID(self._connection, 'cards')
        self._connection.execute(
            """\
                INSERT INTO "cards"
                VALUES(:tsid,:nid,:did,0,:mod,0,0,0,:usn,0,0,0,0,0,0,0,0,'');
            """,
            {
                'tsid': cards_tsid,
                'nid': note_tsid,
                'did': DECK_ID,
                'mod': MODEL_ID,
                'usn': self._get_next_order(),
            }
        )
        self._connection.execute(
            """\
                INSERT INTO "cards"
                VALUES(:tsid,:nid,:did,1,:mod,0,0,0,:usn,0,0,0,0,0,0,0,0,'');
            """,
            {
                'tsid': cards_tsid + 1,
                'nid': note_tsid,
                'did': DECK_ID,
                'mod': MODEL_ID,
                'usn': self._get_next_order(),
            }
        )
        self._connection.execute(
            """\
                INSERT INTO "cards"
                VALUES(:tsid,:nid,:did,2,:mod,0,0,0,:usn,0,0,0,0,0,0,0,0,'');
            """,
            {
                'tsid': cards_tsid + 2,
                'nid': note_tsid,
                'did': DECK_ID,
                'mod': MODEL_ID,
                'usn': self._get_next_order(),
            }
        )
        self._connection.commit()

    def add_media(self, src, name=None):
        if name is None:
            name = os.path.basename(src.name)
        self._media.append(name)
        int_name = str(len(self._media) - 1)
        with open(os.path.join(self._temp_dir.name, int_name), 'wb') as dst:
            shutil.copyfileobj(src, dst)

    def export(self, dst_path):
        self._connection.commit()
        self._connection.close()
        tmpdir = self._temp_dir.name
        with open(os.path.join(tmpdir, 'media'), 'w') as media:
            json.dump(
                {str(n): self._media[n] for n in range(len(self._media))},
                media, sort_keys=True
            )
        with zipfile.ZipFile(dst_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for f in os.listdir(tmpdir):
                zf.write(os.path.join(tmpdir, f), arcname=f)

    def cleanup(self):
        self._temp_dir.cleanup()
