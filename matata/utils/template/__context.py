#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 2019-09-11 23:03:47
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


"""Just now, can't be used in async context
"""

import threading


__stacks = dict()


def _stack():
    tid = threading.get_ident()
    stack = __stacks.get(tid, None)
    if stack is None:
        stack = list()
        __stacks[tid] = stack
    return stack


def push_context():
    stack = _stack()
    stack.append(list())


def pop_context():
    stack = _stack()
    return stack.pop()
