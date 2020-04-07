from flask_script import Manager
from app import app
import sqlite3
from models import User

manager = Manager(app)


@manager.command
def hello():
    print("hello world")


@manager.command
def init_db():
    sql = 'create table user (id INT PRIMARY KEY NOT NULL, pub TEXT, pri TEXT)'
    conn = sqlite3.connect("db/test.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    print('init ok')


@manager.command
def drop_db():
    sql = 'DROP TABLE user'
    conn = sqlite3.connect("db/test.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    print('drop ok')


@manager.command
def save():
    user = User(1, 'pub0', 'pri0')
    user.save()


@manager.command
def query_all():
    users = User.query()
    for user in users:
        print(user.id)
        print(user.pub)
        print(user.pri)


if __name__ == "__main__":
    manager.run()