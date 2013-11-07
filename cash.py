#!/usr/bin/python2
# coding: utf-8
import web
import model

urls = (
        '/', 'Index',
        '/del/(\d+)', 'Delete'
        )


render = web.template.Render('templates', base='base')

class Index:
    form = web.form.Form(
            web.form.Textbox('title', web.form.notnull,
                description=u"项目"),
            web.form.Textbox('yuan',
                web.form.regexp(r"\d+", u"必须是数字"),
                description=u"好多钱？"),
            web.form.Dropdown('type', 
                [u'收入', u'支出'], value=u'支出'),
            web.form.Button("add", html=u'添加'),
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


class Delete:
    def POST(self, id):
        """Delete based on ID"""
        id = int(id)
        model.del_item(id)
        raise web.seeother('/')


app = web.application(urls, globals())


if __name__ == '__main__':
    app.run()
else:
    application = app.wsgifunc()
