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


def count_unique(file_shingles):
    shingles_collection = index_files.load_shingles_collection()
    plagiated_shingles = set()
    plagiated_files = set()
    for shingle in file_shingles:
        for collection_file in shingles_collection.get(shingle, {}):
            plagiated_shingles.add(shingle)
            plagiated_files.add(collection_file)

    return (1 - len(plagiated_shingles) / len(file_shingles)), plagiated_files