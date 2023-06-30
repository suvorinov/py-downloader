# -*- coding: utf-8 -*-
# @Author: Oleg Suvorinov
# @Date:   2023-06-25 09:29:53
# @Last Modified by:   Oleg Suvorinov
# @Last Modified time: 2023-06-25 09:35:51

from typing import Dict

from .http_session import http_session


def get_json(url: str) -> Dict:
    """
    Get the remote file as a dict
    """
    _session = http_session()
    _resp = _session.get(url)
    _resp.raise_for_status()

    try:
        return _resp.json()
    except Exception as e:
        raise e
