from abc import ABCMeta, abstractmethod
from sqlalchemy import create_engine


class AbstractParser(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.data = {}
        super(AbstractParser, self).__init__()

    @abstractmethod
    def parse(self, url, *args):
        pass

    def insert_into_db(self, connection_str, db_table):
        engine = create_engine(connection_str, echo=True)
        conn = engine.connect()
        conn.execute(db_table.insert(), self.data)
