
import re

from pagecounter import config

conf = config.get()

def book_source():
    return conf.book_source

if __name__ == "__main__":
    print(book_source())
