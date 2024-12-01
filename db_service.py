import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

db_path = os.getenv('DB_PATH')


def init():
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS skader (
                    skade_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    skade_type TEXT,
                    skade_pris INTEGER,
                    nummerplade TEXT,
                    syn_type TEXT,
                    indberetnings_dato DATE)
        ''')


        cur.execute('SELECT * FROM skader')
        if not cur.fetchone():
            cur.execute('''
            INSERT INTO skader (skade_type, skade_pris, nummerplade, syn_type, indberetnings_dato)
            VALUES ('Bule', 5000, 'T45L1Q', 'Under Aftale', '2021-02-01'),
                   ('Rids', 2000, 'GXN5A8', 'Efter Aftale', '2021-02-01'),
                   ('Stenslag', 1000, 'G5BEVL', 'Efter Aftale', '2021-02-01')
            ''')



        con.commit()
