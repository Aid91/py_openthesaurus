from py_openthesaurus import OpenThesaurus
import py_openthesaurus.log as log
import argparse

def main():
    logger = log.setup_custom_logger(__name__)

    parser = argparse.ArgumentParser(
        description='Get synonyms of German words from openthesaurus.de')
    parser.add_argument('--word', type=str, action='store', required=True,
                        help="Word from which synonyms will be obtained")
    parser.add_argument('--type', required=False, action='store', choices=['full', 'part'], type=str, default='part',
                        help="Defaults to type=part which meanst that short versions of synonyms will be returned, without nach/zu prefixes/sufixes."
                             "On the other hand type=full returns the full versions of synonyms including nach/zu, sich prefixes")

    args = parser.parse_args()

    open_thesaurus = OpenThesaurus(word=args.word)

    synonyms = open_thesaurus.get_synonyms(type=args.type)

    logger.info(synonyms)

if __name__ == '__main__':
    main()

