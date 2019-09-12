#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 2019-09-10 07:49:32
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

FORGROUND = 'forground', '38'
BACKGROUND = 'background', '48'
FULLCOLOR = '5'


class Style(object):

    __slots__ = ['parent', 'isClear', 'blod', 'dim', 'underline',
                 'blink', 'reverse', 'hidden', 'forground', 'background']

    def __init__(self, parent=None):
        self.parent = parent
        self.isClear = False

    def __str__(self):
        values = []
        for attr in self.__slots__[2:]:
            value = getattr(self, attr, None)
            if value is not None:
                values.append(value)

        if len(values) > 0:
            style = "\033[%sm" % ';'.join(values)
        else:
            style = ""
        if self.isClear is not None:
            return "\033[0m%s" % style
        else:
            return style

    def __repr__(self):
        return self.__str__()

    def _is(self, attr: str):
        value = getattr(self, attr, None)
        if value is not None:
            return value
        elif self.parent is None:
            return None
        else:
            return self.parent._is(attr)

    def _set(self, attr: str, value: str):
        if self.isClear is True and value is not False:
            setattr(self, attr, value)
        else:
            current = self._is(attr)
            if current is None or current is not value:
                setattr(self, attr, value)
        return self

    def setBlod(self, value: bool):
        return self._set('blod', '1' if value is True else '21')

    def setDim(self, value: bool):
        return self._set('dim', '2' if value is True else '22')

    def setUnderline(self, value: bool):
        return self._set('underline', '4' if value is True else '24')

    def setBlink(self, value: bool):
        return self._set('blink', '5' if value is True else '25')

    def setReverse(self, value: bool):
        return self._set('reverse', '7' if value is True else '27')

    def setHidden(self, value: bool):
        return self._set('hidden', '8' if value is True else '28')

    def setColor(self, attr, value, type=None):
        attr, code = attr
        if type is None:
            self._set(attr, "%s" % value)
        else:
            self._set(attr, "%s;%s;%s" % (code, type, value))
        return self

    def clear(self):
        self.blod = None
        self.dim = None
        self.underline = None
        self.blink = None
        self.reverse = None
        self.hidden = None
        self.forground = None
        self.background = None
        self.isClear = True
        return self


class StyledTerminalOutput(object):
    __slots__ = ['style', 'messages']

    def __init__(self):
        self.style = Style()
        self.messages = [self.style]

    def __call__(self, messages: str):
        self.messages.append(messages)
        self.style = Style(self.style)
        self.messages.append(self.style)
        return self

    def __str__(self):
        messages = map(lambda m: str(m), self.messages)
        return ''.join(messages) + '\033[0m'

    def __repr__(self):
        return self.__str__()

    @property
    def clear(self):
        self.style.clear()
        return self

    @property
    def blod(self):
        self.style.setBlod(True)
        return self

    @property
    def dim(self):
        self.style.setDim(True)
        return self

    @property
    def underline(self):
        self.style.setUnderline(True)
        return self

    @property
    def blink(self):
        self.style.setBlink(True)
        return self

    @property
    def reverse(self):
        self.style.setReverse(True)
        return self

    @property
    def hidden(self):
        self.style.setHidden(True)
        return self

    @property
    def unblod(self):
        self.style.setblod(False)
        return self

    @property
    def undim(self):
        self.style.setdim(False)
        return self

    @property
    def ununderline(self):
        self.style.setunderline(False)
        return self

    @property
    def unblink(self):
        self.style.setblink(False)
        return self

    @property
    def unreverse(self):
        self.style.setreverse(False)
        return self

    @property
    def unhidden(self):
        self.style.sethidden(False)
        return self

    def forground(self, color: int, text: str = None):
        """
        设置彩色背景
        color: 1 ~ 256
        """
        self.style.setColor(BACKGROUND, color, FULLCOLOR)
        if text is not None:
            self.__call__(text)
        return self

    def background(self, color: int, text: str = None):
        """
        设置彩色文字
        color: 1 ~ 256
        """
        self.style.setColor(FORGROUND, color, FULLCOLOR)
        if text is not None:
            self.__call__(text)
        return self


if __name__ == "__main__":
    msgs = []
    for row in range(2):
        for column in range(8):
            index = row * 8 + column
            msgs.append("\033[48;5;%sm %4s \033[0m" % (index, index))
        msgs.append("\n")
    msgs.append("\n")
    for row in range(40):
        for column in range(6):
            index = 16 + row * 6 + column
            msgs.append("\033[48;5;%sm %6s \033[0m" % (index, index))
        msgs.append("\n")
    print(''.join(msgs))
