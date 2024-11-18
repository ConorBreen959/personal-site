from flask import flash, request, redirect, url_for
from flask_appbuilder import IndexView, expose


class MyIndexView(IndexView):
    route_base = "/index"

    @expose("/index")
    def index(self):
        return redirect(url_for("PublicView.index"))
