from flask import request
from redis import Redis

from rmc.api.base_resource import BaseResource


class VoteResource(BaseResource):
    name = "vote"
    url = "/vote"

    def post(self):
        r: Redis = self.web_app.redis()

        data = request.get_json(force=True)
        score = int(data["score"])

        if score < 1 or score > 1000:
            return

        token = str(data["voteToken"])
        redis_token = f"rmc:tokens:{token}"

        # get color from token
        if not r.exists(redis_token):
            return

        color = r.get(redis_token).decode()

        pipeline = r.pipeline()
        pipeline.delete(redis_token)
        pipeline.incr(f"rmc:score:{color}", score)
        pipeline.incr(f"rmc:count:{color}", 1)
        pipeline.execute()
        return
