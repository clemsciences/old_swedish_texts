

__author__ = ["Clément Besnier <clemsciences@aol.com>"]
PUNCTUATION = ",;.?!"


def normalize_sentence(sentence: list):
    res = sentence.copy()
    if len(sentence) >= 2:
        if res[-1] in PUNCTUATION:
            res[-2] = res[-2] + res[-1]
            res.pop()
    res[0] = res[0].capitalize()
    return " ".join(res)


if __name__ == "__main__":
    print(normalize_sentence(["bonjour", "ok", "oui", "non", "."]))
