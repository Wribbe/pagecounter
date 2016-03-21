def get():
    import argparse
    config = argparse.Namespace()

    config.book_source = "books.txt"

    return config
