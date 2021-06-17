"""
IE Titanic Utils
"""

__version__ = "0.1.0"  # semver.org

import pandas as pd

import re


def tokenize(text,lower=False, remove_stopwords=False, remove_punctuation=False):
    if text =="":
        raise ValueError("Cannot tokenize empty sentence")
    else:
        if lower:
            text = text.lower()

        if remove_stopwords:
            stopwords = ["a", "the", "or","and"]
            for i in stopwords:
                text = re.sub(r'\s*\b' + i + r'\b\s*', ' ', text).strip()

        if remove_punctuation:
            punctuation = [".", ",", "!"]
            for i in punctuation:
                text = text.replace(i, '')
        text = text.split()

        return text


if __name__ == "__main__":
    print(tokenize("Hello world"))
