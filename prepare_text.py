import collections
import hashlib
import pymorphy2

from nltk import corpus
from exceptions import TooShortText

_morph_analyzer = pymorphy2.MorphAnalyzer()

_STOP_WORDS = corpus.stopwords.words('russian')
_SHINGLE_LEN = 3


def text_to_shingles(text):
    filtered_text = _filter_raw_text(text)
    return _shingle_filtered_text(filtered_text)


def _normalize_word_and_hash(word):
    word_normal_forms = [
        word_info.normal_form
        for word_info in _morph_analyzer.parse(word)
    ]

    normal_forms_counter = collections.Counter(word_normal_forms)
    word_normal_form = normal_forms_counter.most_common(1)[0][0]
    return _hash_str(word_normal_form)


def _hash_str(str_to_hash):
    return hashlib.md5(str_to_hash.encode('utf-8')).hexdigest()


def _filter_raw_text(text):
    filtered_text = ''
    for ch in text:
        if ch.isalpha():
            filtered_text += ch
        else:
            filtered_text += ' '
    
    return filtered_text


def _hash_list(lst):
    m = hashlib.md5()
    for s in lst:
        m.update(s.encode())
    return m.hexdigest()



def _shingle_filtered_text(text):
    list_of_words = [
        _normalize_word_and_hash(word)
        for word in text.split(' ')
        if word and word not in _STOP_WORDS
    ]

    words_num = len(list_of_words)
    if words_num < _SHINGLE_LEN:
        raise TooShortText

    set_of_shingles = set()

    for i in range(words_num + 1 - _SHINGLE_LEN):
        shingle = _hash_list(list_of_words[i:i + _SHINGLE_LEN])
        set_of_shingles.add(shingle)

    return sorted(set_of_shingles)
