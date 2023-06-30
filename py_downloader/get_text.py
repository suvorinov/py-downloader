# -*- coding: utf-8 -*-
# @Author: Oleg Suvorinov
# @Date:   2023-06-25 09:16:46
# @Last Modified by:   Oleg Suvorinov
# @Last Modified time: 2023-06-27 09:03:33

from .http_session import http_session


def get_text(url: str, encoding: str = "") -> str:
    """
    To retrieve the text content
    """
    _session = http_session()
    _resp = _session.get(url)
    _resp.raise_for_status()

    try:
        if encoding:
            _resp.content.decode(encoding)
    except Exception as e:
        raise e
    return _resp.text
