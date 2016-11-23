from enum import Enum
import cian


class Parsers(Enum):
    CIAN = cian.Cian()

if __name__ == '__main__':
    print type(Parsers.CIAN)