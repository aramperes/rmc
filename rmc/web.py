import os
from typing import Type

import redis
from flask import Flask, Blueprint
from flask_restful import Api

from rmc.api.base_resource import BaseResource
from rmc.api.color import ColorResource
from rmc.api.index import IndexResource
from rmc.api.leaderboard import LeaderboardResource
from rmc.api.vote import VoteResource
from rmc.main.about import AboutView
from rmc.main.base_view import BaseView
from rmc.main.index import IndexView
from rmc.main.leaderboard import LeaderboardView


class WebApp:
    def __init__(self, host="127.0.0.1", port=8080, redis_host="127.0.0.1", redis_port=6379):
        self.host = host
        self.port = port
        self.redis_pool = redis.ConnectionPool(host=redis_host, port=redis_port, db=0)

        root_path = os.getcwd()
        static_dir = os.path.join(root_path, "static")
        templates_dir = os.path.join(root_path, "templates")

        self.flask_app = Flask(__name__,
                               root_path=root_path,
                               static_folder=static_dir,
                               template_folder=templates_dir)

        self.blueprint_main = Blueprint("main", __name__, url_prefix="/")
        self.blueprint_api = Blueprint("api", __name__, url_prefix="/api")

        self.api = Api()
        self.register_all()
        self.api.init_app(self.blueprint_api)

        self.flask_app.register_blueprint(self.blueprint_main)
        self.flask_app.register_blueprint(self.blueprint_api)

    def register_all(self):
        # API
        self.register_resource(IndexResource)
        self.register_resource(ColorResource)
        self.register_resource(VoteResource)
        self.register_resource(LeaderboardResource)

        # Main
        self.register_view(IndexView)
        self.register_view(LeaderboardView)
        self.register_view(AboutView)

    def register_view(self, view_class: Type[BaseView]):
        class_setup = view_class.setup(self)
        endpoint = view_class.name
        self.blueprint_main.add_url_rule(
            rule=view_class.url,
            endpoint=endpoint,
            view_func=class_setup.as_view(endpoint)
        )

    def register_resource(self, resource_class: Type[BaseResource]):
        class_setup = resource_class.setup(self)
        endpoint = resource_class.name
        self.api.add_resource(
            class_setup,
            resource_class.url,
            endpoint=endpoint
        )

    def redis(self):
        return redis.Redis(connection_pool=self.redis_pool)

    def run(self):
        self.flask_app.run(
            host=self.host,
            port=self.port,
        )
