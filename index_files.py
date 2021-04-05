import os
import collections
import constants
import prepare_text

from exceptions import IncorrectPath
from pathlib import Path


_PATH_TO_CACHE = '.antiplagiat_cache'


def traverse_files(dir_path):
    if not os.path.exists(dir_path):
        raise IncorrectPath(
            f'Path {dir_path} dosn\'t exist'
        )
    result_dict = collections.defaultdict(set)
    paths_stack = [dir_path]
    while paths_stack:
        cur_dir = paths_stack.pop()
        for dir_item in os.listdir(cur_dir):
            path_to_item = os.path.join(cur_dir, dir_item)
            if os.path.isdir(path_to_item):
                paths_stack.append(path_to_item)
                continue
            _, file_extension = os.path.splitext(path_to_item)
            if file_extension == constants.TXT_EXTENSION:
                with open(path_to_item, 'r') as input_file:
                    raw_text = input_file.read()
                    print(path_to_item)
                    for shingle in prepare_text.text_to_shingles(raw_text):
                        result_dict[shingle].add(path_to_item)

    return dict(result_dict)

def write_to_cache(path_to_docs):
    dict_with_shingles = traverse_files(path_to_docs)
    with open(_PATH_TO_CACHE, 'w') as cache_file:
        cache_file.write(str(dict_with_shingles))

def load_shingles_collection():
    with open(_PATH_TO_CACHE, 'r') as cache_file:
        shingles = cache_file.read()

    return eval(shingles)
