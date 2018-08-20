from weakref import ref


class RouteMixin:
    url = ""
    name = ""

    @classmethod
    def setup(cls, web_app):
        cls._web_app = ref(web_app)
        return cls

    @property
    def web_app(self):
        return self._web_app()
