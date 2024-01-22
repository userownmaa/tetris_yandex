import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect("tetris_db.sqlite")
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS data 
        (result   INTEGER NOT NULL)""")

    def get_data(self):
        data = self.cur.execute("SELECT result FROM data").fetchall()
        for i in range(len(data)):
            data[i] = str(data[i])[1:-2]
        data = list(map(int, data))
        return data

    def add_result(self, res):
        self.cur.execute("INSERT INTO data(result) VALUES(?)", (res,))
        data = self.get_data()
        if len(data) > 1 and len(set(data)) > 1:
            self.cur.execute("DELETE FROM data WHERE result = ?", (min(data),))
        self.con.commit()

    def get_result(self):
        data = self.get_data()
        return data[0]