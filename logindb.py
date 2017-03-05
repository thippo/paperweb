from utils import *

import sqlite3

def _connect_sqlite_db():
     return sqlite3.connect("/data/webdb/login.db")

def confirm_user(username, password):
    cx = _connect_sqlite_db()
    cu = cx.cursor()
    if cu.execute("select * from users where username='"+username+"';").fetchall():
        a = cu.execute("select password from users where username='"+username+"';").fetchall()[0][0]
        cx.close()
        return check_password_hash(a, password)
    else:
        cx.close()
        return False
