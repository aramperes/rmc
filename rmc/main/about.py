from flask import render_template

from rmc.main.base_view import BaseView


class AboutView(BaseView):
    name = "about"
    url = "/about"

    def get(self):
        return render_template("about.html")
