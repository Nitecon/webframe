__author__ = 'Will Hattingh<w.hattingh@nitecon.com>'


class Assembler():
    routes = ""
    urls = ("/.*", "hello")

    def __init__(self, routes):
        self.routes = routes

    def build(self):
        return self.routes