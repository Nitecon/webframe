__author__ = 'Will Hattingh<w.hattingh@nitecon.com>'
import pprint

from RouteAssembler import Assembler


class RouteStack:
    app_path = ''
    config = ''
    urls = ("/.*", "hello")

    def __init__(self, app_path, config):
        self.config = config
        self.app_path = app_path

    def assemble(self):
        #pprint.pprint(self.config['routes'])
        for routes in self.config['routes']:
            pprint.pprint(routes)
            for routename in routes:
                if routes[routename]['type'] == "literal":
                    print "literal route found for:", routename
        return self.urls