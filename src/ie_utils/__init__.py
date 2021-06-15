"""
IE Titanic Utils
"""

__version__ = "0.1.0"  # semver.org

import pandas as pd


def tokenize(text,lower=False):
    if lower:
        text = text.lower()
    return text.split()


if __name__ == "__main__":
    print(tokenize("Hello world"))
