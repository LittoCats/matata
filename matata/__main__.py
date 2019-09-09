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


from matata.utils.command import command, option
import asyncio


@command(prog="matata")
@option('--version', '-v', action="version", version="matata v1.3.7")
async def main(parser, options):
    print('main......')
    count = 5
    while count > 0:
        await asyncio.sleep(1)
        print(f'{count} ......')
        count = count - 1
    print('exit')


@main.subcommand
@option('dev', action="store_true")
@option('--address', help="inet address to bind")
@option('--port', type=int, default=8080, help="port to listen")
async def start(parser, options):
    print('star......')


@main.subcommand
def migrate(parser, options):
    parser.print_help()


@migrate.subcommand(prog='init')
def init_migration(parser, options):
    print('init migration')


@migrate.subcommand(prog='make')
@option('name', nargs='+')
def make_migration(parser, options):
    print('make migration', '_'.join(options.name))


@migrate.subcommand(prog='upgrade')
def upgrade_migration(parser, options):
    print('upgrade migration')


@migrate.subcommand(prog='downgrade')
def downgrade_migration(parser, options):
    print('downgrade migration')


main()
