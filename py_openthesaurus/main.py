from py_openthesaurus import OpenThesaurusWeb
import py_openthesaurus.log as log
import argparse


def main():
    logger = log.setup_custom_logger(__name__)

    parser = argparse.ArgumentParser(
        description='Get synonyms of German words from www.openthesaurus.de')

    parser.add_argument('--form', required=False, action='store', choices=['long', 'short'], type=str, default='short',
                        help="Defaults to form=short which means that short versions of synonyms will be returned, "
                             "without nach/zu prefixes/suffixes."
                             "On the other hand, form=long returns the full versions of synonyms including nach/zu, "
                             "sich prefixes/suffixes")

    required = parser.add_argument_group('required arguments')

    required.add_argument('--word', type=str, action='store', required=True,
                          help="A word from which synonyms will be obtained")

    args = parser.parse_args()

    open_thesaurus = OpenThesaurusWeb()

    synonyms = open_thesaurus.get_synonyms(word=args.word, form=args.form)

    logger.info(synonyms)


if __name__ == '__main__':
    main()
