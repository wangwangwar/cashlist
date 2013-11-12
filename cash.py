#!/usr/bin/env python2
# coding: utf-8

import web
import model

urls = (
        '/', 'Index',
        '/add', 'Add',
        '/admin', 'Admin',
        '/del/(\d+)', 'Delete'
        )


render = web.template.Render('templates', base='base')


class Index:
    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull,
                         description=u"项目", placeholder=u"午餐"),
        web.form.Textbox('yuan',
                         web.form.regexp(r"\d+", u"必须是数字"),
                         description=u"好多钱？", placeholder=u"10"),
        web.form.Dropdown('type',
                          [u'收入', u'支出'], value=u'支出',
                          description=u"类型"),
        web.form.Textbox("submit", html=u'添加'),
    )

    def GET(self):
        """Show page"""
        cash = model.get_cash_details()
        form = self.form()
        return render.index(cash, form)

    def POST(self):
        """Add new entry"""
        form = self.form()
        if not form.validates():
            cash = model.get_cash_details()
            return render.index(cash, form)
        model.new_item(form.d.title, form.d.yuan, form.d.type)
        raise web.seeother('/')


class Add:
    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull,
                         description=u"项目", placeholder=u"午餐"),
        web.form.Textbox('yuan',
                         web.form.regexp(r"\d+", u"必须是数字"),
                         description=u"好多钱？", placeholder=u"10"),
        web.form.Dropdown('type',
                          [u'收入', u'支出'], value=u'支出',
                          description=u"类型"),
        web.form.Textbox("submit", html=u'添加'),
    )

    def GET(self):
        """Show add page."""
        return render.add(self.form)

    def POST(self):
        """Add new entry"""
        form = self.form()
        if not form.validates():
            cash = model.get_cash_details()
            return render.index(cash, form)
        model.new_item(form.d.title, form.d.yuan, form.d.type)
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
