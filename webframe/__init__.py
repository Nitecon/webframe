__author__ = 'Will Hattingh<w.hattingh@nitecon.com>'
import os
import inspect

import web

from router import RouteStack
from config import AppConfig


class Application:
    base_path = ''
    config = ''
    router = ''

    def __init__(self, base_path):
        self.base_path = base_path
        self.config = AppConfig(base_path)


    def get_path(self):
        return self.base_path

    def get_router(self):
        return self.router


base_path = os.path.dirname(os.path.abspath(inspect.stack()[-1][1]))
main_conf = AppConfig(base_path)
app_conf = main_conf.get_config()
router = RouteStack(base_path, app_conf)
urls = router.assemble()
web.config.debug = app_conf['general']['debug']
app = web.application(urls, globals())









