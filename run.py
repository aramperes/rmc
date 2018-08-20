import os

from rmc.web import WebApp

if __name__ == '__main__':
    web_app = WebApp(
        host=os.environ.get("RMC_HOST", default="0.0.0.0"),
        port=int(os.environ.get("RMC_PORT", default=8080)),
        redis_host=os.environ.get("REDIS_HOST", default="127.0.0.1"),
        redis_port=int(os.environ.get("REDIS_PORT", default=6379))
    )
    web_app.run()
