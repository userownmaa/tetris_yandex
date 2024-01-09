import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect("tetris_db.sqlite")
        self.cur = self.con.cursor()

    def add_result(self):
