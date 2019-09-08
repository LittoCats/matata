#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 2019-09-08 21:43:59
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


@command(prog="gossip")
@option("--version", "-v", action='version', version="gossip v1.2.7")
@option("--host", help="server address")
@option("--port", type=int, default=7461, help="server port")
def main(parser, options):
    print(f"connect to server {options.host}:{options.port}")


@main.subcommand(prog='server')
@option("--port", type=int, default=7461, help="server port")
def server(parser, options):
    print(f"start gossip server")


main()
