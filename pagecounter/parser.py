
import re
import sys

from collections import OrderedDict

from pagecounter import config

# Global config object.
conf = config.get()

# Regular expressions.
comment = r'^#'


def parse(data):

    data = data.split('\n')

    non_comment_data = [line for line in data if not re.match(comment,
                        line.strip())]

    title_dict = title_pass(non_comment_data)

    return title_dict


def title_pass(data):

    current_title = ""
    current_data = []

    title_data_dict = OrderedDict()

    for line in data:
        if re.match(r'^\S', line):
            if current_title:
                title_data_dict[current_title] = current_data
                current_data = []
            current_title = line
        else:
            current_data.append(line)

    if current_data:
        title_data_dict[current_title] = current_data

    return title_data_dict


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
