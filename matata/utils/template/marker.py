#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 2019-09-11 23:00:16
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


from .__context import push_context, pop_context


class Marker:

    def __enter__(self):
        push_context()

    def __exit__(self):
        self.children = pop_context()
