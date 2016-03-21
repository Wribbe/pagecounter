
from pagecounter import parser

def test_book_source():
    conf = parser.config.get()
    assert(parser.book_source() == conf.book_source)
