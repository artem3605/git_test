import argparse


def get():
    parser = argparse.ArgumentParser()
    parser.add_argument('type')
    parser.add_argument('-n', '--name')
    return parser.parse_args()

