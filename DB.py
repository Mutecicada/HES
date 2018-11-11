import pymysql


class DataBase:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost',
            user='',
            passwd='',
            db='HES',
            charset='utf8'
        )
        self.cur = None

    def get_cursor(self):
        self.cur = self.db.cursor(pymysql.cursors.DictCursor)

    def db_close(self):
        self.db.close()
