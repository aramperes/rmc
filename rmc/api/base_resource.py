from flask_restful import Resource

from rmc.route_mixin import RouteMixin


class BaseResource(Resource, RouteMixin):
    def __init__(self):
        super(Resource).__init__()
