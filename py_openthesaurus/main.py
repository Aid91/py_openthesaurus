# simple implementation of getting the german synonyms from open thesaurus
import simplejson
import urllib
import translate

UMLAUT_DICTIONARY = {ord(u"ü"): u"ue", ord(u"Ü"): u"Ue", ord(u"ß"): u"ss", ord(u"ä"): u"ae", ord(u"Ä"): u"Ae", ord(u"ö"): u"oe",
           ord(u"Ö"): u"Oe"}

OPEN_THESAURUS_URL = 'http://www.openthesaurus.de/synonyme/search?format=application/json&q=%s'


def get_synonyms(term):
    url = OPEN_THESAURUS_URL % term.translate(UMLAUT_DICTIONARY)
    synonyms = []
    f = urllib.request.urlopen(url)
    ret = simplejson.loads(f.read())

    for cat in ret.get('synsets'):
        synonyms += [synonym.get('term') for synonym in cat.get('terms')]

    return synonyms


if __name__ == '__main__':
    term = 'träumen'
    term = term.translate(UMLAUT_DICTIONARY)

    synonyms = get_synonyms(term)

    print(synonyms)

