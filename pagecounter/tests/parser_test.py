
from .. import parser

def test_hello_world():
    correct = "Hello World"
    assert(parser.hello_world() == correct)
