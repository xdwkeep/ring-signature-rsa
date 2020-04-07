import sqlite3


def get_conn():
    return sqlite3.connect("db/test.db")


class DBfunc():
    @staticmethod
    def init_db():
        sql = 'create table user (id INT PRIMARY KEY NOT NULL, pub TEXT, pri TEXT)'
        conn = sqlite3.connect("db/test.db")
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        print('init ok')

    @staticmethod
    def drop_db():
        sql = 'DROP TABLE user'
        conn = sqlite3.connect("db/test.db")
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        print('drop ok')


class User(object):
    def __init__(self, id, pub, pri):
        self.id = id
        self.pub = pub
        self.pri = pri

    def save(self):
        sql = 'insert into user VALUES (?,?,?)'
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(sql, (self.id, self.pub, self.pri))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def query():
        sql = 'select id, pub, pri from user'
        conn = get_conn()
        cursor = conn.cursor()
        rows = cursor.execute(sql)
        users = []
        for row in rows:
            user = User(row[0], row[1], row[2])
            users.append(user)
        conn.commit()
        cursor.close()
        conn.close()
        return users

