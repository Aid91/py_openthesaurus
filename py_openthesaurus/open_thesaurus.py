from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import simplejson
import log

class OpenThesaurus(object):

    UMLAUT_DICTIONARY = {ord(u"ü"): u"ue", ord(u"Ü"): u"Ue", ord(u"ß"): u"ss", ord(u"ä"): u"ae", ord(u"Ä"): u"Ae",
                         ord(u"ö"): u"oe",
                         ord(u"Ö"): u"Oe"}

    OPEN_THESAURUS_URL = 'http://www.openthesaurus.de/synonyme/search?format=application/json&q=%s'

    def __init__(self, word):
        self.word = word

    def get_synonyms(self):

        logger = log.setup_custom_logger(__name__)

        # TODO: catch all exceptions that can happen when sending such a request
        url = OpenThesaurus.OPEN_THESAURUS_URL % self.word.translate(OpenThesaurus.UMLAUT_DICTIONARY)
        synonyms = []

        try:
            f = urlopen(url)
            ret = simplejson.loads(f.read())

            for cat in ret.get('synsets'):
                synonyms += [synonym.get('term') for synonym in cat.get('terms')]

            return synonyms
        except HTTPError as err:
            return synonyms
            pass
        except URLError as err:
            logger.error("Please check your internet connection! If your internet connection is ok, Open Thesaurus URL or REST API changed!")
            return synonyms
            pass