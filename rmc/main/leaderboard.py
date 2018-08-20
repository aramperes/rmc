from flask import render_template

from rmc.main.base_view import BaseView


class LeaderboardView(BaseView):
    name = "leaderboard"
    url = "/leaderboard"

    def get(self):
        return render_template("leaderboard.html")
