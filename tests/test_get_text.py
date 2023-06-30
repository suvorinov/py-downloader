# -*- coding: utf-8 -*-
# @Author: Oleg Suvorinov
# @Date:   2023-06-25 09:47:24
# @Last Modified by:   Oleg Suvorinov
# @Last Modified time: 2023-06-27 09:01:20

from pprint import pprint

from py_downloader import get_text

_res = get_text('https://cdn.suvorinov.ru/is_alive.txt')
pprint(_res)

_res = get_text('https://cdn.suvorinov.ru/is_alive.html')
pprint(_res)

_res = get_text('http://rutor.info/', encoding='cp1251')
pprint(_res)
