import pymysql


class DataBase:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            db='HES',
            charset='utf8'
        )
        self.cur = self.db.cursor(pymysql.cursors.DictCursor)
