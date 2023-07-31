import sqlite3


class Database:
    
    def create(self):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS articles (source, title, date, text)")
        con.commit()
