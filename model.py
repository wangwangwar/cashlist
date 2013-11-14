# coding: utf-8
import web

db = web.database(dbn='sqlite', db='cash.sqlite')

def get_cash_details():
    return db.select('cash', order='id')


def new_item(date, item, yuan, type):
    q = db.insert('cash', date=date, title=item, yuan=yuan, type=type)


def del_item(id):
    db.delete('cash', where="id=$id", vars=locals())
