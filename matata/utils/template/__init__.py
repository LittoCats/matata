#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 2019-09-11 21:37:08
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

"""这是一个想法，不需要额外解析的模板语言，仅依赖 python with 语句

可以这样定义一个 index 页面:

```python
from matata.utils.template import Html, Head, Script, Style, Body, Div, Label, Input, Button

def main():
    with Html():
        Head.Meta()
        Head.Title("Matata")
        Script(src="https://ichvv.com/matata.py")
        Head.Meta(name="tabby:email" content="littocats@gmail.com")
        Style(href="https://ichvv.com/matata.css")
        Style('''
        body: {
            padding: 0;
            margin: 0;
        }
        ''')
        Script('''
        !function() { console.log("Hakuna matata!") }()
        ''')
        with Body():
            with Panel():
                Label("username:")
                Input(name='username', type='text')
            with Panel():
                Label("password:")
                Input(name='password', type='password')
            Button('Submit', type="submit")


```

可以这样定义一个组件：

```
class LoginView(View):
    def render(self):
        with Container():
            with Panel():
                Label("username:")
                Input(name='username', type='text')
            with Panel():
                Label("password:")
                Input(name='password', type='password')
```

所有的一切者一标准的 python 代码；

受 React 语法影响，本来有类似 pyx 的想法，但即刻转念，python 语法本就挺好的。
"""
