# -*- coding: utf-8 -*-
# @Author: suvorinov
# @Date:   2023-06-15 10:19:33
# @Last Modified by:   Oleg Suvorinov
# @Last Modified time: 2023-06-30 07:58:37

import os
import sys
from urllib3 import util
from urllib.parse import urlparse
from math import log, ceil
import pprint

import hashlib

import requests
from requests import adapters
from tqdm import tqdm

from py_random_useragent import UserAgent

"""Перенести в проект py_utils
"""

def is_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def url2filename(url: str) -> str:
    fragment_removed = url.split("#")[0]  # keep to left of first #
    query_string_removed = fragment_removed.split("?")[0]
    scheme_removed = query_string_removed.split("://")[-1].split(":")[-1]
    if scheme_removed.find("/") == -1:
        return ""
    return os.path.basename(scheme_removed)


class Downloader(object):
    """docstring for Downloader
    """
    def __init__(self):
        super(Downloader, self).__init__()


    def __url_to_downloadable(self, url: str) -> str:
        """Convert a url to the proper style depending on its website."""

        if "drive.google.com" in url:
            # For future support of google drive
            file_id = url.split("d/")[1].split("/")[0]
            base_url = "https://drive.google.com/uc?export=download&id="
            out = "{}{}".format(base_url, file_id)
        elif "dropbox.com" in url:
            if url.endswith(".png"):
                out = url + "?dl=1"
            else:
                out = url.replace("dl=0", "dl=1")
        else:
            out = url
        return out

    def save(self, url, path: str = "", overwrite: bool = False) -> str:
        pass

    def run(self) -> str:
        try:
            _dir = os.path.dirname(self.__download_path)
            if _dir and not os.path.isdir(_dir):
                os.makedirs(_dir)
        except Exception as e:
            raise e

        _session = self.__session()
        resp = _session.get(self.__url, stream=True)
        resp.raise_for_status()
        total = int(resp.headers.get('Content-Length', 0))
        pprint.pprint(resp.headers)
        if self.__verbose:
            tqdm.write(
                "Downloading data from %s (%s)"
                % (self.__url, human_sizeof(total)),
                file=sys.stdout,
            )
        with open(self.__download_path, 'wb') as file, tqdm(
            desc=self.__download_path,
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
            disable=not self.__verbose
        ) as bar:
            for data in resp.iter_content(chunk_size=Downloader.chunk_size):
                size = file.write(data)
                # if self.__verbose:
                bar.update(size)

        tqdm.write(f"Successfully downloaded {self.__download_file} from {self.__url}.") # noqa
        return self.__download_path
