import sqlite3 as sl
con = sl.connect('users.sql')
cursor = con.cursor()
class user:
    name:       str
    login:      str
    password:   str
    tscore:     int
    rpsscore:   int
us=user()
   


def new (log: str, passw: str):
    sql = 'INSERT INTO users ( login,    password, tscore,   rpsscore ) values(?, ?, ?, ?)'
    data = [
        (log, passw, 0, 0)
    ]
    with con:
        con.executemany(sql, data)
def load (log: str):
    cursor.execute("SELECT login,    password, tscore,  rpsscore  FROM users WHERE login=?", [(log)])
    us=user()
    temp = (cursor.fetchone())
    if (temp is None):
        return -1
    us.login     =temp[0]
    us.password   = temp[1]
    us.tscore    = temp[2]
    us.rpsscore   = temp[3]
    return us

print(load('23').tscore)