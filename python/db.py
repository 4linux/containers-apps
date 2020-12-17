#!/usr/bin/python3

import pymysql

from os import environ as env
from flask import current_app, g

def get_db():
    '''Obtém a conexão com o banco.

    g é uma variável global do Flask.
    Caso nenhuma conexão tenha sido criada até então, uma nova
    conexão é criada, guardada em g.db e retornada.
    Chamadas subsequentes da mesma requisição utilizarão a conexão 
    criada anteriormente dentro de g.db.'''
    if 'db' not in g:
        g.db = pymysql.connect(
            host       = env['DB_HOST'],
            db         = env['DB_NAME'],
            user       = env['DB_USER'],
            passwd     = env['DB_PASS'],
            autocommit = True
        )
    return g.db

def close_db():
    '''Remove db da variável g e fecha a conexão'''
    db = g.pop('db')
    if db:
        db.close()

def init_app(current_app):
    '''Fecha a conexão com o banco a cada fim de requisição'''
    app.teardown_appcontext(close_db)
