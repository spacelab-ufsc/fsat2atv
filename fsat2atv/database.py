#
#  database.py
#  
#  Copyright The FloripaSat-2A Telemetry Viewer Contributors.
#  
#  This file is part of FloripaSat-2A Telemetry Viewer.
#
#  FloripaSat-2A Telemetry Viewer is free software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#  
#  FloripaSat-2A Telemetry Viewer is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public
#  License along with FloripaSat-2A Telemetry Viewer; if not, see
#  <http://www.gnu.org/licenses/>.
#  
#

import sqlite3

class Database:

    def __init__(self, filename):
        """
        Database class.

        :return: None
        """
        self._filename = filename
        self._ts = None
        self._create_table(self._filename)

    def _create_table(self, filename):
        with sqlite3.connect(filename) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS telemetries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME NOT NULL,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL,
                    value TEXT NOT NULL,
                    unit TEXT NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')

    def set_timestamp(self, ts):
        self._ts = ts

    def get_timestamp(self):
        return self._ts

    def write(self, name, tp, value, unit):
        """
        Write data to a database.

        :return: None
        """
        with sqlite3.connect(self._filename) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO telemetries (timestamp, name, type, value, unit) VALUES (?, ?, ?, ?, ?)", (self.get_timestamp(), name, tp, value, unit))

    def read(self):
        with sqlite3.connect(self._filename) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM telemetries")
            rows = cursor.fetchall()

            # Get column names
            column_names = [description[0] for description in cursor.description]

            print("\nData in telemetries:")
            print("-" * 80)
            print(" | ".join(column_names))
            print("-" * 80)

            for row in rows:
                print(" | ".join(str(cell) for cell in row))
