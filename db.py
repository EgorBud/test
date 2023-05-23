import sqlite3 as sl
con = sl.connect('users.sql')
with con:
    con.execute("""
       CREATE TABLE IF NOT EXISTS users(
            name TEXT,
            login TEXT PRIMARY KEY,
            password TEXT,
            tscore INTEGER,
            rpsscore INTEGER,
            age INTEGER
        );
    """)
con.close()