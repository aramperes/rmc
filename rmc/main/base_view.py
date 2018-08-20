from flask.views import MethodView

from rmc.route_mixin import RouteMixin


class BaseView(MethodView, RouteMixin):
    def __init__(self):
        super(MethodView).__init__()
