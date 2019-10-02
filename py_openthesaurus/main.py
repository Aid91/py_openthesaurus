# simple implementation of getting the german synonyms from open thesaurus
from open_thesaurus import OpenThesaurus
import log

if __name__ == '__main__':
    logger = log.setup_custom_logger(__name__)

    word = 'träumen'
    word = word.translate(OpenThesaurus.UMLAUT_DICTIONARY)

    open_thesaurus = OpenThesaurus(word=word)

    synonyms = open_thesaurus.get_synonyms()

    logger.info(synonyms)

