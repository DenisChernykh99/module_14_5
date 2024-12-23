import sqlite3


def initiate_db():
    """Инициализация базы данных и создание таблицы Products."""
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    # Создаем таблицу Products, если она еще не существует
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                price INTEGER NOT NULL
            )
        ''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL
            )
    ''')

    conn.commit()
    conn.close()


def add_user(username, email, age):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute(f'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (username, email, age, 1000))

    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    # Проверяем, есть ли пользователь с таким именем
    cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    result = cursor.fetchone()

    conn.close()

    return bool(result)


def get_all_products():
    """Получение всех записей из таблицы Products."""
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    conn.close()
    return products

# initiate_db()
# conn = sqlite3.connect("products.db")
# cursor = conn.cursor()

# Добавляем несколько тестовых продуктов
# cursor.execute("INSERT INTO Products (title, description, price) VALUES ('Продуктивин', 'Для повышения продуктивности.', 100)")
# cursor.execute("INSERT INTO Products (title, description, price) VALUES ('UrbanУчизм', 'Специально для учеников Urban.', 200)")
# cursor.execute("INSERT INTO Products (title, description, price) VALUES ('Баттизмулин', 'Специально для ТГ ботов.', 300)")
# cursor.execute("INSERT INTO Products (title, description, price) VALUES ('Батарейквизм', 'Для зарядки батареек.', 400)")

# conn.commit()
# conn.close()
