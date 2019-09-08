#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 2019-09-08 16:15:04
# @AUTHOR  : 程巍巍 (littocats@gmail.com)
#
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.


from argparse import *
import os


def migrate_init(options):
    print(f"migrate: {options}")


def migrate_make(options):
    print(f"migrate: {options}")


def migrate_upgrade(options):
    print(f"migrate: {options}")


def migrate_downgrade(options):
    print(f"migrate: {options}")


def test(options):
    print(f"op: {options}")


def start(options):
    print(f"o: {options}")


def main():
    parser = ArgumentParser(prog='matata')
    parser.set_defaults(func=lambda x: parser.print_help())
    parser.add_argument('--version', '-v', action='version', version='matata 1.0.11')
    subparsers = parser.add_subparsers(title='commands')

    # database migration
    migrator = subparsers.add_parser('migrate')
    migrator.set_defaults(func=lambda x: migrator.print_help())

    migrators = migrator.add_subparsers(title='commands')

    initmigrator = migrators.add_parser('init')
    initmigrator.set_defaults(func=migrate_init)
    initmigrator.add_argument('workdir', nargs='?', default=os.getcwd())

    makemigrator = migrators.add_parser('make')
    makemigrator.set_defaults(func=migrate_make)
    makemigrator.add_argument('name', nargs='?')

    upgrademigrator = migrators.add_parser('upgrade')
    upgrademigrator.set_defaults(func=migrate_upgrade)

    downgrademigrator = migrators.add_parser('downgrade')
    downgrademigrator.set_defaults(func=migrate_downgrade)

    # Test
    testor = subparsers.add_parser('test')
    testor.set_defaults(func=test)

    startor = subparsers.add_parser('start')
    startor.set_defaults(func=start)

    startor.add_argument('dev', nargs='?', default=False, type=bool)
    startor.add_argument('--debug', action='store_true')
    startor.add_argument('--autoreload', action='store_true')
    startor.add_argument('--port', default=8080, type=int)

    options = parser.parse_args()
    options.func(options)


main()
