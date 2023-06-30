# -*- coding: utf-8 -*-
# @Author: suvorinov
# @Date:   2023-06-21 14:30:43
# @Last Modified by:   Oleg Suvorinov
# @Last Modified time: 2023-06-24 07:45:21

import sys
import os

from tqdm import tqdm

from py_utils import human_sizeof

from .http_session import http_session
from .filename_from_url import filename_from_url


CHUNK_SIZE = 1024


def download(
    url,
    output_path: str = "",
    overwrite: bool = False,
    verbose: bool = False
) -> str:
    """
    Download and save a remote file

    Parameters
    ----------
    url : string
        The url of the file to download.
    output_path : string
        The path where the downloaded file will be stored.
    owerwrite : bool
        If True the local file will be overwritten,
        False will skip the download.
    verbose : bool
        Whether to print download status to the screen.

    Returns
    -------
    out_path : string
        A path to the downloaded file (or folder, in the case of
        a zip file).
    """

    _filename_from_url = filename_from_url(url)
    if output_path or output_path.endswith(os.path.sep):
        if not os.path.exists(output_path):
            os.makedirs(output_path)
    output_path = os.path.join(output_path, _filename_from_url)

    _session = http_session()
    resp = _session.get(url, stream=True)
    resp.raise_for_status()
    total = int(resp.headers.get('Content-Length', 0))
    if verbose:
        tqdm.write(
            "Downloading data from %s (%s)"
            % (url, human_sizeof(total)),
            file=sys.stdout,
        )
    try:
        with open(output_path, 'wb') as file, tqdm(
            desc=_filename_from_url,
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
            disable=not verbose
        ) as bar:
            for chunk in resp.iter_content(chunk_size=CHUNK_SIZE):
                size = file.write(chunk)
                # if self.__verbose:
                bar.update(size)
    except Exception as e:
        raise e
    else:
        if verbose:
            tqdm.write(f"Successfully downloaded {_filename_from_url} from {url}.")  # noqa
    finally:
        _session.close()
        if verbose:
            bar.close()

    return output_path
