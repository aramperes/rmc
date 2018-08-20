from rmc.api.base_resource import BaseResource


class IndexResource(BaseResource):
    url = "/"
    name = "index"

    def get(self):
        return {
            "success": True
        }
