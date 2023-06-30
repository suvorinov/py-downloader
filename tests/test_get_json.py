# -*- coding: utf-8 -*-
# @Author: Oleg Suvorinov
# @Date:   2023-06-25 09:39:55
# @Last Modified by:   Oleg Suvorinov
# @Last Modified time: 2023-06-25 09:46:29

from pprint import pprint

from py_downloader import get_json

_res = get_text('https://cdn.suvorinov.ru/is_alive.txt')
pprint(_res)
