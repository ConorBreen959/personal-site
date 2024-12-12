from flask import g, render_template, redirect, url_for, flash, request
from flask_appbuilder import BaseView, has_access, expose, PublicFormView
from flask_appbuilder.widgets import ListWidget
from flask_login import current_user

from app import appbuilder
from app.forms import ContactForm
from app.utils import send_email


class PublicWidget(ListWidget):
    template = "index.html"


class PublicView(BaseView):
    route_base = "/"
    # edit_widget = PublicWidget

    @expose("/", methods=['GET', 'POST'])
    def contact(self):
        form = ContactForm()
        if form.validate_on_submit():
            name = request.form.get("name")
            email = request.form.get("email")
            message = request.form.get("message")
            captcha = request.form.get("recaptcha")
            name, email, message = (text if text else "<blank>" for text in [name, email, message])
            send_email(name, email, message)
            flash("Email sent", "info")
        return self.render_template("index.html", form=form)


class HomeView(BaseView):
    route_base = "/home"

    @has_access
    @expose("/user/")
    def user(self):
        user = g.user

        if user.is_anonymous:
            return redirect(url_for("AuthDBView.login"))
        greeting = f"Hello {current_user}"
        return self.render_template("logged_user.html", greeting=greeting)


class HealthView(BaseView):
    route_base = "/health"

    @expose("/check/")
    def check(self):
        greeting = "Hello World"
        return self.render_template("logged_user.html", greeting=greeting)


@appbuilder.app.after_request
def add_header(response):
    response.cache_control.private = True
    response.cache_control.public = False
    response.headers["Cache-Control"] = "no-store, max-age=0"
    return response


@appbuilder.app.errorhandler(500)
def page_not_found(e):
    return (
        render_template(
            "server_error.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        500,
    )


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )
