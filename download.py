"""

"""
import bz2
import os

from requests import get


__author__ = ["Clément Besnier <clemsciences@aol.com>"]


def download_spraakbanken_corpora():
    """

    :return:
    """
    folder = "corpora"
    files = "files"
    if not os.path.exists(os.path.join(os.getcwd(), files)):
        os.mkdir(files)
    if not os.path.exists(os.path.join(os.getcwd(), folder)):
        os.mkdir(folder)

    links = ["http://spraakbanken.gu.se/lb/resurser/meningsmangder/fsv-verser.xml.bz2",
             "http://spraakbanken.gu.se/lb/resurser/meningsmangder/fsv-aldrelagar.xml.bz2",
             "http://spraakbanken.gu.se/lb/resurser/meningsmangder/fsv-aldrereligiosprosa.xml.bz2",
             "http://spraakbanken.gu.se/lb/resurser/meningsmangder/fsv-yngretankebocker.xml.bz2",
             "http://spraakbanken.gu.se/lb/resurser/meningsmangder/fsv-yngrelagar.xml.bz2"]
    for link in links:
        xml_data = get(link).content
        with open(os.path.join(files, link.split("/")[-1]), "wb") as f:
            f.write(xml_data)
        with open(os.path.join(files, link.split("/")[-1]), "rb") as f:
            data = bz2.decompress(f.read())
            with open(os.path.join(folder, link.split("/")[-1].split(".bz2")[0]), "wb") as f:
                f.write(data)


if __name__ == "__main__":
    download_spraakbanken_corpora()
