
test_book_data = """
#This is a comment
Title of book

  Tags: Tag1, tag2, abcd
  Total: 700
  Exam: !today+7

  Sections:

    date: !today+1
    0 [2-5]: 0-10

    date: !today+2
    1 [1,2]: 10-20

    date: !today+3
    1 [3-5]: 21-30

Title of second book

Title of third book
"""

from pagecounter import parser

def test_titles():

    parser_result = parser.parse(test_book_data)

    title_list = [
            'Title of book',
            'Title of second book',
            'Title of third book',
            ]

    assert(list(parser_result.keys()) == title_list)
