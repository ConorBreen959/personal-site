from flask import flash, request, redirect, url_for
from flask_appbuilder import IndexView, expose

from app.utils import send_email


class MyIndexView(IndexView):
    route_base = "/"
    default_view = "index"

    @expose("/")
    def index(self):
        return self.render_template("index.html")

    @expose("/contact/", methods=['GET', 'POST'])
    def contact(self):
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        name, email, message = (text if text else "<blank>" for text in [name, email, message])
        send_email(name, email, message)
        flash("Email sent", "info")
        return redirect(url_for("MyIndexView.index"))


class MyBaseView(IndexView):
    index_template = "my_base.html"
