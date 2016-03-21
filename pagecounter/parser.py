
import re
import sys

from pagecounter import config

conf = config.get()


def parse(data):

    return {}

def main(args):

    if args:
        book_source = args[0]
    else:
        book_source = conf.book_source

    with open(book_source, 'r') as file_pointer:
        book_data = file_pointer.read()

    parse(book_data)

if __name__ == "__main__":
    main(sys.argv[1:])
