import os

import collections

import index_files
import prepare_text

from exceptions import IncorrectPath

def prepare_doc(file_path):
    if not os.path.exists(file_path):
        raise IncorrectPath(
            f'Path {dir_path} dosn\'t exist'
        )

    with open(file_path, 'r') as input_file:
        raw_text = input_file.read()
        print(file_path)
        shingles = prepare_text.text_to_shingles(raw_text)

    return shingles


def count_unique(file_path):
    file_shingles = prepare_doc(file_path)
    shingles_collection = index_files.load_shingles_collection()
    dict_of_uniqueness = collections.defaultdict(int)
    for shingle in file_shingles:
        for collection_file in shingles_collection.get(shingle, {}):
            dict_of_uniqueness[collection_file] += 1

    return dict_of_uniqueness