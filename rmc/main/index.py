from flask import render_template

from rmc.main.base_view import BaseView


class IndexView(BaseView):
    name = "index"
    url = "/"

    def get(self):
        return render_template("index.html", socket_host=self.web_app.socket_host)
