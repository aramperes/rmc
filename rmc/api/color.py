import random
import secrets

from redis import Redis

from rmc.api.base_resource import BaseResource
from rmc.colors import get_week_colors, hex_color, is_dark


class ColorResource(BaseResource):
    name = "color"
    url = "/color"

    def get(self):
        r: Redis = self.web_app.redis()

        vote_token = secrets.token_urlsafe(50)
        color_index = random.randint(0, 256)
        color = get_week_colors(max_gen=color_index)[-1]
        color_hex = hex_color(color)

        r.set(f"rmc:tokens:{vote_token}", color_hex, ex=60 * 10)

        light_text = is_dark(color)

        return {
            "colorHex": "#" + color_hex,
            "voteToken": vote_token,
            "lightText": light_text
        }
