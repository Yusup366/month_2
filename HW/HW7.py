import sqlite3

def connect_or_create_db():
    return sqlite3.connect('user_with_grades.db')

def create_table():
    connect = connect_or_create_db()
    cursor = connect.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            fio VARCHAR(100) NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    connect.commit()
    connect.close()

def add_user(fio, age):
    connect = connect_or_create_db()
    cursor = connect.cursor()
    cursor.execute(
        'INSERT INTO users(fio, age) VALUES (?, ?)',
        (fio, age)
    )
    connect.commit()
    connect.close()

def get_user_by_id(userid):
    connect = connect_or_create_db()
    cursor = connect.cursor()

    cursor.execute('SELECT fio, age FROM users WHERE userid = ?', (userid,))
    user = cursor.fetchone()

    if user:
        print(f'Пользователь с ID {userid}: {user[0]}, {user[1]} лет')
    else:
        print(f'Пользователь с ID {userid} не найден')

    connect.close()

create_table()

add_user('Олег', 35)
add_user('Егор', 33)
add_user('Игорь', 32)

get_user_by_id(2)