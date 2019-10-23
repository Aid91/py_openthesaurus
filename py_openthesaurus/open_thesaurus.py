from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json
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

    def get_synonyms(self, form="short"):

        logger = log.setup_custom_logger(__name__)

        try:

            if self.is_entry_word_valid():
                url = self.url % self.word.translate(self.umlaut_dictionary)
                request = Request(url)
                with urlopen(request) as response:
                    return self._get_synonyms_from_response(response, form)
            else:
                logger.warn('Please provide a valid (non empty, non null) input word!')
                return []
        except URLError:
            logger.error(
                "Please check your internet connection! If your internet connection is ok, Open Thesaurus URL or REST "
                "API changed!")
            return []
        except RuntimeError as runtime_error:
            logger.error(repr(runtime_error))
            return []
        except Exception as exception:
            logger.error(repr(exception))
            return []

    def _get_synonyms_from_response(self, response, form):
        synonyms = []

        response_raw = response.read()

        # decode the response to add support for python 3.5
        response_decoded = response_raw.decode('utf-8')
        json_response = json.loads(response_decoded)

        for category in json_response.get("synsets"):
            synonyms += self._get_synonyms_from_category(category=category, form=form)

        return synonyms

    def _get_synonyms_from_category(self, category, form):

        long_form_regex = r"[()]"
        short_form_regex = r"[\(].*?[\)]"

        if form == "long":
            return [re.sub(long_form_regex, "", synonym.get("term")).strip() for synonym in category.get("terms")]
        elif form == "short":
            return [re.sub(short_form_regex, "", synonym.get("term")).strip() for synonym in category.get("terms")]
        else:
            raise RuntimeError("Form is not valid! Please choose form to be either: long or short")
