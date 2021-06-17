import pytest

import pandas as pd

from numpy.testing import assert_array_almost_equal

from ie_utils import tokenize

@pytest.mark.parametrize("sentence, expected_tokens",[
    ("This is a sentence", ["This","is","a","sentence"]),
    ("Another sentence", ["Another","sentence"])
])
def test_tokenize_returns_expected_list(sentence, expected_tokens):
    tokens = tokenize(sentence)

    assert tokens == expected_tokens
    
def test_tokenize_returns_lowercase_tokens():
    sentence = "This is a sentence"

    expected_tokens = ["this","is","a","sentence"]
    
    assert expected_tokens == tokenize(sentence, lower=True) 
    
def test_series_are_approximately_equal():
    ser = pd.Series([0.1,0.2,0.1+0.2])
    expected_ser = pd.Series([0.1,0.2,0.3])
    
    assert_array_almost_equal(ser, expected_ser)
    
def test_tokenize_returns_tokens_without_stopwords():
    sentence = "and this is a one sentence or the other"

    expected_tokens = ["this","is","one","sentence","other"]
    
    assert expected_tokens == tokenize(sentence, remove_stopwords=True)  
    
def test_tokenize_returns_tokens_without_punctuation():
    sentence = "This, is a sentence. One sentence!"

    expected_tokens = ["This","is","a","sentence","One","sentence"]
    
    assert expected_tokens == tokenize(sentence, remove_punctuation=True) 
    
def test_ValueError():
    with pytest.raises(ValueError, match="Cannot tokenize empty sentence"):
        tokenize("")