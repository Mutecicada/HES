import pymysql


class DataBase:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            passwd='028358kk',
            db='HES',
            charset='utf8'
        )
        self.cur = None

    def get_cur(self):
        self.cur = self.db.cursor(pymysql.cursors.DictCursor)

    def db_close(self):
        self.db.close()
