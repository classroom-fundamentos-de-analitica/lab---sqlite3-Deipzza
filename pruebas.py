import sqlite3
import sys

import pandas as pd


def load_data():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    with open("create_tables.sql", encoding="utf-8") as file:
        cur.executescript(file.read())

    return conn, cur

def test_01():
    conn, _ = load_data()
    with open("pregunta_01.sql", encoding="utf-8") as file:
        query = file.read()
    return pd.read_sql_query(query, conn)

def test_02():
    conn, _ = load_data()
    with open("pregunta_02.sql", encoding="utf-8") as file:
        query = file.read()
    return pd.read_sql_query(query, conn)

def test_03():
    conn, _ = load_data()
    with open("pregunta_03.sql", encoding="utf-8") as file:
        query = file.read()
    return pd.read_sql_query(query, conn)

def test_04():
    conn, _ = load_data()
    with open("pregunta_04.sql", encoding="utf-8") as file:
        query = file.read()
    return pd.read_sql_query(query, conn)

def test_05():
    conn, _ = load_data()
    with open("pregunta_05.sql", encoding="utf-8") as file:
        query = file.read()
    return pd.read_sql_query(query, conn)

def test_06():
    conn, _ = load_data()
    with open("pregunta_06.sql", encoding="utf-8") as file:
        query = file.read()
    return pd.read_sql_query(query, conn)

def test_07():
    conn, _ = load_data()
    with open("pregunta_07.sql", encoding="utf-8") as file:
        query = file.read()
    return pd.read_sql_query(query, conn)

def test_08():
    conn, _ = load_data()
    with open("pregunta_08.sql", encoding="utf-8") as file:
        query = file.read()
    return pd.read_sql_query(query, conn)

def test_09():
    conn, _ = load_data()
    with open("pregunta_09.sql", encoding="utf-8") as file:
        query = file.read()
    return pd.read_sql_query(query, conn)

def test_10():
    conn, _ = load_data()
    with open("pregunta_10.sql", encoding="utf-8") as file:
        query = file.read()
    return pd.read_sql_query(query, conn)

def test_11():
    conn, _ = load_data()
    with open("pregunta_11.sql", encoding="utf-8") as file:
        query = file.read()
    return pd.read_sql_query(query, conn)

def test_12():
    conn, _ = load_data()
    with open("pregunta_12.sql", encoding="utf-8") as file:
        query = file.read()
    return pd.read_sql_query(query, conn)

def test_13():
    conn, _ = load_data()
    with open("pregunta_13.sql", encoding="utf-8") as file:
        query = file.read()
    return pd.read_sql_query(query, conn)

def test_14():
    conn, _ = load_data()
    with open("pregunta_14.sql", encoding="utf-8") as file:
        query = file.read()
    return pd.read_sql_query(query, conn)

