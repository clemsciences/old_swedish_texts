"""

"""

from bs4 import BeautifulSoup
from xml.etree import ElementTree
import codecs

from utils import normalize_sentence

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


def read_moses():
    with open('texts/moses.html', 'r') as f:
        b = BeautifulSoup(f.read(), 'html5lib')

    print(b.text[1000:2100])


def read_corpus():
    with codecs.open("corpora/fsv-aldrelagar.xml", "r", encoding="utf8") as f:
        text = f.read()

    root = ElementTree.fromstring(text)
    ltext = []
    for text in root:
        title = text.attrib["title"]
        print(title)
        lparagraph = []
        for paragraph in text:
            sentences = []
            for sentence in paragraph:
                lsentence = []
                for word in sentence:
                    lsentence.append(word.text)
                sentences.append(normalize_sentence(lsentence))
            lparagraph.append(" ".join(sentences))
        # print("\n\n".join(lparagraph))
        ltext.append("\n\n".join(lparagraph))
    return ltext


if __name__ == "__main__":
    print(read_corpus()[0])
