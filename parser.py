# -*- coding: utf-8 -*-

from reparsers.cian import Cian


class Parser(object):

    def __init__(self, site):
        self.concrete_parser = site

    def parse(self, url):
        return self.concrete_parser.parse(url=url)

