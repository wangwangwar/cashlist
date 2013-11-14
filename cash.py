#!/usr/bin/env python2
# coding: utf-8

import web
import model
import datetime

urls = (
        '/', 'Index',
        '/add', 'Add',
        '/admin', 'Admin',
        '/del/(\d+)', 'Delete'
        )


render = web.template.Render('templates', base='base')


class Index:
    """Index page, """
    def GET(self):
        """Show page"""
        cash = model.get_cash_details()
        return render.index(cash)


class Add:

    def GET(self):
        """Show add page."""
        return render.add(today=datetime.date.today())

    def POST(self):
        """Add new entry."""
        post = web.input()
        model.new_item(post.date, post.item, post.yuan, post.type)
        raise web.seeother('/')


class Delete:
    def POST(self, id):
        """Delete based on ID"""
        id = int(id)
        model.del_item(id)
        raise web.seeother('/admin')


class Admin:

    def GET(self):
        """Show page"""
        cash = model.get_cash_details()
        return render.admin(cash)


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
else:
    application = app.wsgifunc()
