#!/usr/bin/python3

import pymysql
from db import get_db, close_db
from faker import Faker
from flask import Flask, render_template

faker = Faker()

app = Flask(__name__)
app.teardown_appcontext(close_db) # chama close_db a cada fim de execução

@app.route('/')
def home():

    con = get_db()
    cur = con.cursor(pymysql.cursors.DictCursor)
    try:
        cur.execute('INSERT INTO usuarios (nome, email) VALUES (%s, %s)', (faker.name(), faker.email()))
    except pymysql.err.ProgrammingError as ex:
        cur.execute('CREATE TABLE IF NOT EXISTS usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), email VARCHAR(255))')

    cur.execute('SELECT * FROM usuarios')
    usuarios = cur.fetchall()
    return render_template('index.html', usuarios=usuarios)
