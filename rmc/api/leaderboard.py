from flask import request
from redis import Redis

from rmc.api.base_resource import BaseResource
from rmc.colors import get_week_colors, hex_color, is_dark


class LeaderboardResource(BaseResource):
    url = "/leaderboard"
    name = "leaderboard"

    def get(self):
        r: Redis = self.web_app.redis()
        week = request.args.get("week", default=None, type=int)

        colors = get_week_colors(week=week)

        pipeline = r.pipeline()
        for color in colors:
            pipeline.get(f"rmc:colors:{hex_color(color)}")

        scores = pipeline.execute()

        leaderboard = [
            {
                "color": "#" + hex_color(colors[i]),
                "score": int(scores[i].decode()) if scores[i] else 0,
                "lightText": is_dark(colors[i])
            }
            for i in range(len(colors))
        ]

        def comparator(x):
            return x["score"]

        return sorted(leaderboard, key=comparator, reverse=True)
