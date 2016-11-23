# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
from socket import timeout
import sys
import time
from abstract_parser import AbstractParser

__classes__ = [
    'serp-item__price-col',
    'serp-item__type-col',
    'serp-item__area-col',
    'serp-item__floor-col'
]


class Cian(AbstractParser):
    def __init__(self):
        super(Cian, self).__init__()

    def _load_page(self, url):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        try:
            thing = opener.open(url, None, 10)
            soup = BeautifulSoup(thing.read(), "lxml")
            if soup is None:
                print "soup is None"
                self._load_page(url)
            else:
                return soup
        except (timeout, urllib2.HTTPError, urllib2.URLError) as error:
            sys.stdout.write("{} encountered".format(error))
            sys.stdout.flush()
            time.sleep(30)
            self._load_page(url)

    def parse(self,
              url,
              description=False):
        soup = self._load_page(url)
        divs = soup.find_all(attrs={'ng-class': "{'serp-item_removed': offer.remove.state, "
                                                "'serp-item_popup-opened': isPopupOpen}"})
        for div in divs:
            pass

    @staticmethod
    def _get_item_solid(class_name, div):
        target_class = div.find(class_name)
        return target_class.find(attrs={'class': 'serp-item__solid'}).get_text().strip()

    @staticmethod
    def _get_items_prop(class_name, div):
        target_class = div.find(class_name)
        result = []
        props = target_class.find_all(attrs={'class': 'serp-item__prop'})
        for prop in props:
            result.append(prop.get_text().strip())
        return result

    @staticmethod
    def _get_id(div):
        return div.find(attrs={'class': 'serp-item__realtor js-serp-item-realtor-trigger'}).get_text().strip()

    @staticmethod
    def _get_description(div):
        return div.find(attrs={'class': 'serp-item__description__text js-serp-item-description-text'})\
                    .get_text().strip()

    @staticmethod
    def _get_address(div):
        return div.find(attrs={'class': 'serp-item__address-precise'}).get_text().strip()

    @staticmethod
    def _get_metro(div):
        tmp = div.find(attrs={'class': 'serp-item__solid serp-item__metro'})
        return tmp.find('a').get_text().strip()

    @staticmethod
    def _get_distance(div):
        return div.find(attrs={'class': 'serp-item__distance'}).get_text().strip()