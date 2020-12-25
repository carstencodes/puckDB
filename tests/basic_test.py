#
# Copyright (c) 2020 Carsten Igel.
#
# This file is part of puckdb
# (see https://github.com/carstencodes/puckdb).
#
# License: 3-clause BSD, see https://opensource.org/licenses/BSD-3-Clause
#

import unittest
import tempfile
import os
import time

import puckdb


class BasicTest(unittest.TestCase):
    def test_no_crash(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file: str = os.path.join(str(tmp_dir), "test.db")
            db = puckdb.PuckDB(file, True, False)
            db.set("test", 1)
            time.sleep(2)  # Wait for worker to complete
            db2 = puckdb.PuckDB(file, False, False)
            value = db2.get("test")
            print(db2.getall())
            self.assertEqual(value, 1)


if __name__ == "__main__":
    unittest.main()
