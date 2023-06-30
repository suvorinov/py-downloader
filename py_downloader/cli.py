# -*- coding: utf-8 -*-
# @Author: suvorinov
# @Date:   2023-06-20 13:06:47
# @Last Modified by:   suvorinov
# @Last Modified time: 2023-06-22 10:49:59

import argparse
import pkg_resources

from py_downloader.download import download


def main(args=None):

    _prog = "%(prog)s"
    _version = pkg_resources.get_distribution('py_downloader').version
    _prog_version = f"{_prog} {_version}"

    # Initialize parser
    parser = argparse.ArgumentParser(
        prog='downloder',
        description='A simple Downloader written in Python'
    )

    parser.add_argument(
        "url",
        help="URL to download",
        # required=True
    )

    parser.add_argument(
        "-v",
        "--verbose",
        help="show progress bar and console log",
        action="store_true")

    parser.add_argument(
        "-o",
        "--output-path",
        help=("path of the directory to download the file, "
              "default is '' (i.e. current directory)"
              ),
        default="",
        type=str
    )

    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=_prog_version
    )
    args = parser.parse_args()

    file_name = download(
        args.url,
        args.output_path,
        verbose=args.verbose
    )

    print(file_name)


if __name__ == '__main__':
    main()
