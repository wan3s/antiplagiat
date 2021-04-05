import argparse

import analize_doc
import index_files
import prepare_text

from pprint import pprint


def main():
    parser = argparse.ArgumentParser(description='My own plagiat detecting system')
    parser.add_argument(
        '--index',
        help='Index docs; don\'t forget to specify path(s) to docs!',
        nargs='+',
    )
    parser.add_argument(
        '--check',
        help=(
            'Detect plagiat in your doc; don\'t '
            'forget to specify path(s) to your doc(s)!'
        ),
        nargs=1,
    )
    args = parser.parse_args()
    if args.index:
        for raw_docs_path in args.index:
            print(f'indexing {raw_docs_path}...')
            index_files.write_to_cache(raw_docs_path)
            print('... successfully finished!')
    if args.check:
        for file_to_check_path in args.check:
            print(f'checking {file_to_check_path}...')
            print(analize_doc.count_unique(file_to_check_path))


if __name__ == '__main__':
    main()
