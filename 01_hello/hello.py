#!/usr/bin/env python3
'''
Author: Haziel Sanchez <haziel.sanchez.pe@gmail.com>
Purpose: Say hello
'''

import argparse


def get_args():
    '''Get the commands-line arguments'''
    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('-n', '--name', metavar='name', default='World',
                        help='Name to greet')
    return parser.parse_args()


def main():
    '''It's just a main function'''
    args = get_args()
    print('Hello, '+args.name+'!')


if __name__ == '__main__':
    main()
