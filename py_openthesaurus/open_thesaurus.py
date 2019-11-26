from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json
import re
from abc import ABC
from abc import abstractmethod

import py_openthesaurus.log as log
from py_openthesaurus.mysql_wrapper import MySQLWrapper


class OpenThesaurusBase(ABC):

    def __init__(self):
        self.umlaut_dictionary = {ord(u"ü"): u"ue", ord(u"Ü"): u"Ue", ord(u"ß"): u"ss", ord(u"ä"): u"ae",
                                  ord(u"Ä"): u"Ae",
                                  ord(u"ö"): u"oe",
                                  ord(u"Ö"): u"Oe"}
        self.logger = log.setup_custom_logger(__name__)
        self.url = "http://www.openthesaurus.de/synonyme/search?format=application/json&q=%s"
        self.db_query = ("SELECT term.word FROM term, synset, term term2 WHERE synset.is_visible = 1 AND synset.id = \n"
                         "term.synset_id AND term2.synset_id = synset.id AND term2.word = '%s'")

    def is_entry_word_valid(self, word):
        if word is None:
            return False

        regex = r"[^a-zA-Z]+"
        word_ = re.sub(regex, "", word)
        return word_ is not ""

    @abstractmethod
    def get_synonyms(self, word, form="short"):
        pass


class OpenThesaurusWeb(OpenThesaurusBase):

    def get_synonyms(self, word, form="short"):

        try:
            if self.is_entry_word_valid(word):
                url = self.url % word.translate(self.umlaut_dictionary)
                request = Request(url)
                with urlopen(request) as response:
                    return self._get_synonyms_from_response(response, form)
            else:
                self.logger.warning('Please provide a valid (non empty, non null) input word, instead of word: (%s)',
                                    word)
                return []
        except URLError:
            self.logger.error(
                "Please check your internet connection! If your internet connection is ok, Open Thesaurus URL or REST "
                "API changed or you have reached the maximum of 60 requests per minute!")
            return []
        except RuntimeError as runtime_error:
            self.logger.error(repr(runtime_error))
            return
        except Exception as exception:
            self.logger.error(repr(exception))
            return []

    def _get_synonyms_from_response(self, response, form):
        synonyms = []
        response_raw = response.read()

        # decode the response to add support for python 3.5
        response_decoded = response_raw.decode('utf-8')
        json_response = json.loads(response_decoded)

        for category in json_response.get("synsets"):
            synonyms += self._get_synonyms_from_category(
                category=category, form=form)

        return synonyms

    def _get_synonyms_from_category(self, category, form):

        long_form_regex = r"[()]"
        short_form_regex = r"[\(].*?[\)]"

        if form == "long":
            return [re.sub(long_form_regex, "", synonym.get("term")).strip()
                    for synonym in category.get("terms")]
        elif form == "short":
            return [re.sub(short_form_regex, "", synonym.get("term")).strip()
                    for synonym in category.get("terms")]
        else:
            raise RuntimeError(
                "Form is not valid! Please choose form to be either: long or short")


class OpenThesaurusDb(OpenThesaurusBase):

    def __init__(self, host, db_name, user, passwd):
        super(OpenThesaurusDb, self).__init__()
        self._connect_db(host, db_name, user, passwd)

    def _connect_db(self, host, db_name, user, passwd):
        self.mysql_db = MySQLWrapper(
            host=host, db=db_name, user=user, passwd=passwd)

    def get_synonyms(self, word, form="short"):

        try:
            if self.is_entry_word_valid(word):
                query = self.db_query % word
                synonyms = self.mysql_db.select_all(query=query)
                synonyms = [
                    "%s" %
                    synonym_tupple for synonym_tupple in synonyms]
                return self._get_synonyms_based_on_form(synonyms, form=form)
            else:
                self.logger.warning('Please provide a valid (non empty, non null) input word, instead of word: (%s)',
                                    word)
                return []
        except URLError:
            self.logger.error(
                "Please check your internet connection! If your internet connection is ok, Open Thesaurus URL or REST "
                "API changed or you have reached the maximum of 60 requests per minute!")
            return []
        except RuntimeError as runtime_error:
            self.logger.error(repr(runtime_error))
            return
        except Exception as exception:
            self.logger.error(repr(exception))
            return []

    def _get_synonyms_based_on_form(self, synonyms, form):

        long_form_regex = r"[()]"
        short_form_regex = r"[\(].*?[\)]"

        if form == "long":
            return [re.sub(long_form_regex, "", synonym).strip()
                    for synonym in synonyms]
        elif form == "short":
            return [re.sub(short_form_regex, "", synonym).strip()
                    for synonym in synonyms]
        else:
            raise RuntimeError(
                "Form is not valid! Please choose form to be either: long or short")
