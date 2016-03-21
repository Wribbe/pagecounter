
import re

from . import config

conf = config.get()

def book_source():
    return conf.book_source
