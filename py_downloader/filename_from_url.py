# -*- coding: utf-8 -*-
# @Author: Oleg Suvorinov
# @Date:   2023-06-22 09:19:16
# @Last Modified by:   suvorinov
# @Last Modified time: 2023-06-22 09:20:00

import os


def filename_from_url(url: str) -> str:
    fragment_removed = url.split("#")[0]  # keep to left of first #
    query_string_removed = fragment_removed.split("?")[0]
    scheme_removed = query_string_removed.split("://")[-1].split(":")[-1]
    if scheme_removed.find("/") == -1:
        return ""
    return os.path.basename(scheme_removed)
