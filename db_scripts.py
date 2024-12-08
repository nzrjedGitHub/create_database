# questions = [
#     ('Яка тварина є найбільшим сухопутним ссавцем?', 'Слон', 'Жирафа', 'Ведмідь', 'Конь'),
#     ('Яка тварина є символом Австралії?', 'Кенгуру', 'Коала', 'Ему', 'Пінгвін'),
#     ('Яка тварина може спати до 20 годин на день?', 'Лев', 'Коала', 'Мишка', 'Зебра'),
#     ('Яка тварина відома своєю здатністю змінювати колір?', 'Хамелеон', 'Змія', 'Жаба', 'Летючий дракон'),
#     ('Яка тварина є найбільшим морським ссавцем?', 'Кит', 'Акула', 'Дельфін', 'Морж'),
#     ('Яка тварина може літати, але не є птахом?', 'Летюча миша', 'Кажан', 'Крилатий змій', 'Комар')
# ]


import sqlite3
db_name = 'quiz.sqlite'
conn = None
curor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def clear_db():
    ''' видаляє всі таблиці '''
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS question'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()

    
def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')


    do('''CREATE TABLE IF NOT EXISTS quiz (
           id INTEGER PRIMARY KEY,
           name VARCHAR)''')
    
    do('''CREATE TABLE IF NOT EXISTS question (
               id INTEGER PRIMARY KEY,
               question VARCHAR,
               answer VARCHAR,
               wrong1 VARCHAR,
               wrong2 VARCHAR,
               wrong3 VARCHAR)''')
    
    do('''CREATE TABLE IF NOT EXISTS quiz_content (
               id INTEGER PRIMARY KEY,
               quiz_id INTEGER,
               question_id INTEGER,
               FOREIGN KEY (quiz_id) REFERENCES quiz (id),
               FOREIGN KEY (question_id) REFERENCES question (id) )''')
    close()

def add_questions():
    questions = [
    ('Яка тварина є найбільшим сухопутним ссавцем?', 'Слон', 'Жирафа', 'Ведмідь', 'Конь'),
    ('Яка тварина є символом Австралії?', 'Кенгуру', 'Коала', 'Ему', 'Пінгвін'),
    ('Яка тварина може спати до 20 годин на день?', 'Лев', 'Коала', 'Мишка', 'Зебра'),
    ('Яка тварина відома своєю здатністю змінювати колір?', 'Хамелеон', 'Змія', 'Жаба', 'Летючий дракон'),
    ('Яка тварина є найбільшим морським ссавцем?', 'Кит', 'Акула', 'Дельфін', 'Морж'),
    ('Яка тварина може літати, але не є птахом?', 'Летюча миша', 'Кажан', 'Крилатий змій', 'Комар')
]
    open()
    cursor.executemany('''INSERT INTO question
                        (question, answer, wrong1, wrong2, wrong3)
                        VALUES (?,?,?,?,?)''', questions)
    conn.commit()
    close()

def add_quiz():
    quizes = [
        ('Своя гра', ),
        ('Хто хоче стати мільйонером?', ),
        ('Найрозумніший', )
    ]
    open()
    cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quizes)
    conn.commit()
    close()

def show(table):
    query = 'SELECT * FROM ' + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    close()

def show_tables():
    show('question')
    show('quiz')
    show('quiz_content')

def main():
    clear_db()
    create()
    add_questions()
    show_tables()

if __name__ == "__main__":
    main()
