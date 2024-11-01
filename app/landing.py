from flask_appbuilder import IndexView, expose


class MyIndexView(IndexView):
    route_base = "/"

    @expose("/")
    def index(self):
        return self.render_template("index.html")


class MyBaseView(IndexView):
    index_template = "my_base.html"
