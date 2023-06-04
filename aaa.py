
import sqlite3 as sl

con = sl.connect('users.sql')
cursor = con.cursor()

cursor.execute("SELECT login,    password, tscore,  rpsscore  FROM users WHERE login=?", [("man")])
temp = (cursor.fetchone())
print(temp)
log="man"
sql = "UPDATE users SET rpsscore = (rpsscore + 1) WHERE login=?"
with con:
    try:
        con.execute(sql, [log])
    except Exception as e:
        print(e)
cursor.execute("SELECT login,    password, tscore,  rpsscore  FROM users WHERE login=?", [("man")])
temp = (cursor.fetchone())
print(temp)

