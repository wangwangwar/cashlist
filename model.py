# coding: utf-8
import web
import datetime

db = web.database(dbn='sqlite', db='cash.sqlite')

def get_cash_details():
    return db.select('cash', order='id')


def new_item(text, cash, type):
    q = db.insert('cash', title=text, yuan=cash, type=type, date=datetime.date.today())


def del_item(id):
    db.delete('cash', where="id=$id", vars=locals())
