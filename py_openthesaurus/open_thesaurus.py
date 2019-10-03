from urllib.request import urlopen
from urllib.error import URLError
import simplejson
import py_openthesaurus.log as log
import re

class OpenThesaurus(object):

    def __init__(self, word):
        self.word = word
        self.umlaut_dictionary = {ord(u"ü"): u"ue", ord(u"Ü"): u"Ue", ord(u"ß"): u"ss", ord(u"ä"): u"ae",
                                  ord(u"Ä"): u"Ae",
                                  ord(u"ö"): u"oe",
                                  ord(u"Ö"): u"Oe"}
        self.url = "http://www.openthesaurus.de/synonyme/search?format=application/json&q=%s"

    def is_entry_word_valid(self):

        if self.word is None:
            return False

        regex = r"[^a-zA-Z]+"
        word = re.sub(regex, "", self.word)
        return word is not ""

    def get_synonyms(self, type="part"):

        logger = log.setup_custom_logger(__name__)

        try:

            if self.is_entry_word_valid():
                url = self.url % self.word.translate(self.umlaut_dictionary)
                with urlopen(url) as response:
                    return self._get_synonyms_from_response(response, type)
            else:
                logger.warn('Please provide a valid (non empty, non null) input word!')
                return []
        except URLError:
            logger.error(
                "Please check your internet connection! If your internet connection is ok, Open Thesaurus URL or REST "
                "API changed!")
            return []
        except RuntimeError as re:
            logger.error(repr(re))
            return []
        except Exception as ex:
            logger.error(repr(ex))
            return []

    def _get_synonyms_from_response(self, response, type):
        synonyms = []
        json_response = simplejson.loads(response.read())

        for category in json_response.get("synsets"):
            synonyms += self._get_synonyms_from_category(category=category, type=type)

        return synonyms

    def _get_synonyms_from_category(self, category, type):

        full_regex = r"[()]"
        part_regex = r"[\(].*?[\)]"

        if type == "full":
            return [re.sub(full_regex, "", synonym.get("term")).strip() for synonym in category.get("terms")]
        elif type == "part":
            return [re.sub(part_regex, "", synonym.get("term")).strip() for synonym in category.get("terms")]
        else:
            raise RuntimeError("Type is not valid! Please choose type to be either: full or part")
