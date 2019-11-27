import unittest
from unittest.mock import MagicMock, patch

from py_openthesaurus import OpenThesaurusDb


class OpenThesaurusDbTest(unittest.TestCase):

    @patch('py_openthesaurus.open_thesaurus.MySQLWrapper')
    def test_entry_word_valid_german(self, mysql_db_mock):
        # arrange
        word = 'München'
        mysql_db_mock.return_value = MagicMock()

        # act
        instance = OpenThesaurusDb(host="localhost", user="dummy", passwd="dummy", db_name="dummy_db")
        valid = instance.is_entry_word_valid(word=word)

        # assert
        self.assertTrue(valid)

    @patch('py_openthesaurus.open_thesaurus.MySQLWrapper')
    def test_entry_word_not_valid_none(self, mysql_db_mock):
        # arrange
        word = None
        mysql_db_mock.return_value = MagicMock()

        # act
        instance = OpenThesaurusDb(host="localhost", user="dummy", passwd="dummy", db_name="dummy_db")
        valid = instance.is_entry_word_valid(word=word)

        # assert
        self.assertFalse(valid)

    @patch('py_openthesaurus.open_thesaurus.MySQLWrapper')
    def test_entry_word_not_valid_all_special_charaters(self, mysql_db_mock):
        # arrange
        word = '!!!$!!!"??'
        mysql_db_mock.return_value = MagicMock()

        # act
        instance = OpenThesaurusDb(host="localhost", user="dummy", passwd="dummy", db_name="dummy_db")
        valid = instance.is_entry_word_valid(word=word)

        # assert
        self.assertFalse(valid)

    @patch('py_openthesaurus.open_thesaurus.MySQLWrapper')
    def test_entry_word_not_valid(self, mysql_db_mock):
        # arrange
        word = ''
        mysql_db_mock.return_value = MagicMock()

        # act
        instance = OpenThesaurusDb(host="localhost", user="dummy", passwd="dummy", db_name="dummy_db")
        valid = instance.is_entry_word_valid(word=word)

        # assert
        self.assertFalse(valid)

    @patch('py_openthesaurus.open_thesaurus.MySQLWrapper')
    def test_entry_word_valid_special_characters(self, mysql_db_mock):
        # arrange
        word = 'Taking!"WDSDA sadsad!!!'
        mysql_db_mock.return_value = MagicMock()

        # act
        instance = OpenThesaurusDb(host="localhost", user="dummy", passwd="dummy", db_name="dummy_db")
        valid = instance.is_entry_word_valid(word=word)

        # assert
        self.assertTrue(valid)

    @patch('py_openthesaurus.open_thesaurus.MySQLWrapper')
    def test_entry_word_valid(self, mysql_db_mock):
        # arrange
        word = 'Taking'
        mysql_db_mock.return_value = MagicMock()

        # act
        instance = OpenThesaurusDb(host="localhost", user="dummy", passwd="dummy", db_name="dummy_db")
        valid = instance.is_entry_word_valid(word=word)

        # assert
        self.assertTrue(valid)

    @patch('py_openthesaurus.open_thesaurus.MySQLWrapper')
    def test_get_synonyms_empty_no_word_in_dictionary(self, mysql_db_mock):
        # arrange
        word = 'Taking'
        mysql_db_mock.return_value.select_all.return_value = []

        # act
        instance = OpenThesaurusDb(host="localhost", user="dummy", passwd="dummy", db_name="dummy_db")
        synonyms = instance.get_synonyms(word=word)

        # assert
        self.assertFalse(synonyms)

    @patch('py_openthesaurus.open_thesaurus.MySQLWrapper')
    def test_get_synonyms_empty_wrong_input_word(self, mysql_db_mock):
        # arrange
        word = ''
        mysql_db_mock.return_value.select_all.return_value = (
        ('should',), ('not',), ('be',), ('taken',), ('into',), ('account',))

        # act
        instance = OpenThesaurusDb(host="localhost", user="dummy", passwd="dummy", db_name="dummy_db")
        synonyms = instance.get_synonyms(word=word)

        # assert
        self.assertFalse(synonyms)

    @patch('py_openthesaurus.open_thesaurus.MySQLWrapper')
    def test_get_synonyms_empty_wrong_input_word_special_characters(self, mysql_db_mock):
        # arrange
        word = None
        mysql_db_mock.return_value.select_all.return_value = (
        ('should',), ('not',), ('be',), ('taken',), ('into',), ('account',))

        # act
        instance = OpenThesaurusDb(host="localhost", user="dummy", passwd="dummy", db_name="dummy_db")
        synonyms = instance.get_synonyms(word=word)

        # assert
        self.assertFalse(synonyms)

    @patch('py_openthesaurus.open_thesaurus.MySQLWrapper')
    def test_get_synonyms_long_not_empty(self, mysql_db_mock):
        # arrange
        word = 'gehen'

        mysql_db_mock.return_value.select_all.return_value = (
            ('(es) tun',), ('klappen',), ('funzen',), ('funktionieren',), ('laufen',), ('gehen',), ('funktionuckeln',),
            ('latschen',), ('zu Fuß laufen',), ('gehen',), ('zu Fuß gehen',), ('einen Fuß vor den anderen setzen',),
            ('laufen',), ('in Betracht kommen',), ('möglich sein',), ('gehen',), ('zur Debatte stehen',),
            ('zur Diskussion stehen',), ('in Frage kommen',), ('drin sein',), ('(sich) machen lassen',),
            ('machbar sein',),
            ('infrage kommen',), ('über die Klinge springen (lassen)',), ('abtreten',), ('sein Leben aushauchen',),
            ('in die Grube fahren',), ('ableben',), ('den Geist aufgeben',), ('sterben',), ('seinen Geist aufgeben',),
            ('seinen Geist aushauchen',), ('dahinscheiden',), ('sein Leben lassen',), ('fallen',), ('ins Gras beißen',),
            ('dahingehen',), ('das Zeitliche segnen',), ('davongehen',), ('entschlafen',), ('sanft entschlafen',),
            ('von uns gehen',), ('verscheiden',), ('versterben',), ('von der Bühne des Lebens abtreten',),
            ('verdämmern',),
            ('erlöschen',), ('uns verlassen',), ('(seine) letzte Fahrt antreten',),
            ('in die ewigen Jagdgründe eingehen',),
            ('seinen letzten Gang gehen',), ('(jemandes) letztes Stündlein hat geschlagen',),
            ('dran glauben (müssen)',),
            ('(den) Arsch zukneifen',), ('in den letzten Zügen liegen',), ('dahingerafft werden (von)',), ('gehen',),
            ('(die) Augen für immer schließen',), ('(den) Weg allen Fleisches gehen',), ('(die) Reihen lichten sich',),
            ('wegsterben',), ('die Hufe hochreißen',), ('vor seinen Richter treten',), ('vor seinen Schöpfer treten',),
            ('(jemandem) schlägt die Stunde',), ('(den) Löffel abgeben',), ('aus dem Leben scheiden',),
            ('ins Grab sinken',), ('(seinen) Abschied nehmen',), ('(ein Unternehmen) verlassen',), ('weggehen',),
            ('kündigen',), ('künden',), ('aufhören (bei)',), ('was Besseres finden',), ('seinen Hut nehmen',),
            ('(den Kram) hinschmeißen',), ('(den) Job an den Nagel hängen',), ('(sich) was anderes suchen',),
            ('(den) Bettel hinschmeißen',), ('(den) Dienst quittieren',), ('ausscheiden',), ('gehen',),
            ('in den Sack hauen',), ('das Handtuch werfen',), ('(sein) Bündel schnüren',),
            ('(eine) neue Herausforderung suchen (Bewerbungssprache)',), ('(sein) Büro räumen',),
            ('(seine) Kündigung einreichen',), ('(sich) entfernen',), ('weggehen',), ('verschwinden',), ('abhauen',),
            ('(sich) davon machen',), ('(sich) zurückziehen',), ('enteilen',), ('(sich) rausscheren',),
            ('(einen) Rückzieher machen',), ('(sich) von dannen machen',), ('abzischen',))

        # act
        instance = OpenThesaurusDb(host="localhost", user="dummy", passwd="dummy", db_name="dummy_db")
        synonyms = instance.get_synonyms(word=word, form='long')

        # assert
        self.assertTrue(synonyms)

    @patch('py_openthesaurus.open_thesaurus.MySQLWrapper')
    def test_get_synonyms_short_not_empty(self, mysql_db_mock):
        # arrange
        word = 'gehen'

        mysql_db_mock.return_value.select_all.return_value = (
            ('(es) tun',), ('klappen',), ('funzen',), ('funktionieren',), ('laufen',), ('gehen',), ('funktionuckeln',),
            ('latschen',), ('zu Fuß laufen',), ('gehen',), ('zu Fuß gehen',), ('einen Fuß vor den anderen setzen',),
            ('laufen',), ('in Betracht kommen',), ('möglich sein',), ('gehen',), ('zur Debatte stehen',),
            ('zur Diskussion stehen',), ('in Frage kommen',), ('drin sein',), ('(sich) machen lassen',),
            ('machbar sein',),
            ('infrage kommen',), ('über die Klinge springen (lassen)',), ('abtreten',), ('sein Leben aushauchen',),
            ('in die Grube fahren',), ('ableben',), ('den Geist aufgeben',), ('sterben',), ('seinen Geist aufgeben',),
            ('seinen Geist aushauchen',), ('dahinscheiden',), ('sein Leben lassen',), ('fallen',), ('ins Gras beißen',),
            ('dahingehen',), ('das Zeitliche segnen',), ('davongehen',), ('entschlafen',), ('sanft entschlafen',),
            ('von uns gehen',), ('verscheiden',), ('versterben',), ('von der Bühne des Lebens abtreten',),
            ('verdämmern',),
            ('erlöschen',), ('uns verlassen',), ('(seine) letzte Fahrt antreten',),
            ('in die ewigen Jagdgründe eingehen',),
            ('seinen letzten Gang gehen',), ('(jemandes) letztes Stündlein hat geschlagen',),
            ('dran glauben (müssen)',),
            ('(den) Arsch zukneifen',), ('in den letzten Zügen liegen',), ('dahingerafft werden (von)',), ('gehen',),
            ('(die) Augen für immer schließen',), ('(den) Weg allen Fleisches gehen',), ('(die) Reihen lichten sich',),
            ('wegsterben',), ('die Hufe hochreißen',), ('vor seinen Richter treten',), ('vor seinen Schöpfer treten',),
            ('(jemandem) schlägt die Stunde',), ('(den) Löffel abgeben',), ('aus dem Leben scheiden',),
            ('ins Grab sinken',), ('(seinen) Abschied nehmen',), ('(ein Unternehmen) verlassen',), ('weggehen',),
            ('kündigen',), ('künden',), ('aufhören (bei)',), ('was Besseres finden',), ('seinen Hut nehmen',),
            ('(den Kram) hinschmeißen',), ('(den) Job an den Nagel hängen',), ('(sich) was anderes suchen',),
            ('(den) Bettel hinschmeißen',), ('(den) Dienst quittieren',), ('ausscheiden',), ('gehen',),
            ('in den Sack hauen',), ('das Handtuch werfen',), ('(sein) Bündel schnüren',),
            ('(eine) neue Herausforderung suchen (Bewerbungssprache)',), ('(sein) Büro räumen',),
            ('(seine) Kündigung einreichen',), ('(sich) entfernen',), ('weggehen',), ('verschwinden',), ('abhauen',),
            ('(sich) davon machen',), ('(sich) zurückziehen',), ('enteilen',), ('(sich) rausscheren',),
            ('(einen) Rückzieher machen',), ('(sich) von dannen machen',), ('abzischen',))

        # act
        instance = OpenThesaurusDb(host="localhost", user="dummy", passwd="dummy", db_name="dummy_db")
        synonyms = instance.get_synonyms(word=word)

        # assert
        self.assertTrue(synonyms)

    @patch('py_openthesaurus.open_thesaurus.MySQLWrapper')
    def test_get_synonyms_long_short(self, mysql_db_mock):
        # arrange
        word = 'gehen'
        mysql_db_mock.return_value.select_all.return_value = (
            ('(es) tun',), ('klappen',), ('funzen',), ('funktionieren',), ('laufen',), ('gehen',), ('funktionuckeln',),
            ('latschen',), ('zu Fuß laufen',), ('gehen',), ('zu Fuß gehen',), ('einen Fuß vor den anderen setzen',),
            ('laufen',), ('in Betracht kommen',), ('möglich sein',), ('gehen',), ('zur Debatte stehen',),
            ('zur Diskussion stehen',), ('in Frage kommen',), ('drin sein',), ('(sich) machen lassen',),
            ('machbar sein',),
            ('infrage kommen',), ('über die Klinge springen (lassen)',), ('abtreten',), ('sein Leben aushauchen',),
            ('in die Grube fahren',), ('ableben',), ('den Geist aufgeben',), ('sterben',), ('seinen Geist aufgeben',),
            ('seinen Geist aushauchen',), ('dahinscheiden',), ('sein Leben lassen',), ('fallen',), ('ins Gras beißen',),
            ('dahingehen',), ('das Zeitliche segnen',), ('davongehen',), ('entschlafen',), ('sanft entschlafen',),
            ('von uns gehen',), ('verscheiden',), ('versterben',), ('von der Bühne des Lebens abtreten',),
            ('verdämmern',),
            ('erlöschen',), ('uns verlassen',), ('(seine) letzte Fahrt antreten',),
            ('in die ewigen Jagdgründe eingehen',),
            ('seinen letzten Gang gehen',), ('(jemandes) letztes Stündlein hat geschlagen',),
            ('dran glauben (müssen)',),
            ('(den) Arsch zukneifen',), ('in den letzten Zügen liegen',), ('dahingerafft werden (von)',), ('gehen',),
            ('(die) Augen für immer schließen',), ('(den) Weg allen Fleisches gehen',), ('(die) Reihen lichten sich',),
            ('wegsterben',), ('die Hufe hochreißen',), ('vor seinen Richter treten',), ('vor seinen Schöpfer treten',),
            ('(jemandem) schlägt die Stunde',), ('(den) Löffel abgeben',), ('aus dem Leben scheiden',),
            ('ins Grab sinken',), ('(seinen) Abschied nehmen',), ('(ein Unternehmen) verlassen',), ('weggehen',),
            ('kündigen',), ('künden',), ('aufhören (bei)',), ('was Besseres finden',), ('seinen Hut nehmen',),
            ('(den Kram) hinschmeißen',), ('(den) Job an den Nagel hängen',), ('(sich) was anderes suchen',),
            ('(den) Bettel hinschmeißen',), ('(den) Dienst quittieren',), ('ausscheiden',), ('gehen',),
            ('in den Sack hauen',), ('das Handtuch werfen',), ('(sein) Bündel schnüren',),
            ('(eine) neue Herausforderung suchen (Bewerbungssprache)',), ('(sein) Büro räumen',),
            ('(seine) Kündigung einreichen',), ('(sich) entfernen',), ('weggehen',), ('verschwinden',), ('abhauen',),
            ('(sich) davon machen',), ('(sich) zurückziehen',), ('enteilen',), ('(sich) rausscheren',),
            ('(einen) Rückzieher machen',), ('(sich) von dannen machen',), ('abzischen',))

        # act
        instance = OpenThesaurusDb(host="localhost", user="dummy", passwd="dummy", db_name="dummy_db")
        synonyms_short = instance.get_synonyms(word=word)
        synonyms_long = instance.get_synonyms(word=word, form='long')

        # assert
        synonyms_long_len = len(".".join(synonyms_long))
        synonyms_short_len = len(".".join(synonyms_short))

        self.assertLessEqual(synonyms_short_len, synonyms_long_len)

    @patch('py_openthesaurus.open_thesaurus.MySQLWrapper')
    def test_get_synonyms_long_short_equal(self, mysql_db_mock):
        # arrange
        word = 'München'
        mysql_db_mock.return_value.select_all.return_value = (
            ('bayerische Landeshauptstadt',), ('Minga',), ('München',), ('bayerische Metropole',),
            ('Weltstadt mit Herz',),
            ('Bayernmetropole',))

        # act
        instance = OpenThesaurusDb(host="localhost", user="dummy", passwd="dummy", db_name="dummy_db")
        synonyms_short = instance.get_synonyms(word=word)
        synonyms_long = instance.get_synonyms(word=word, form='long')

        # assert
        synonyms_long_len = len(".".join(synonyms_long))
        synonyms_short_len = len(".".join(synonyms_short))

        self.assertLessEqual(synonyms_short_len, synonyms_long_len)

    @patch('py_openthesaurus.open_thesaurus.MySQLWrapper')
    def test_runtime_error_wrong_type(self, mysql_db_mock):
        # arrange
        word = 'München'
        mysql_db_mock.return_value.select_all.return_value = (
            ('bayerische Landeshauptstadt',), ('Minga',), ('München',), ('bayerische Metropole',),
            ('Weltstadt mit Herz',),
            ('Bayernmetropole',))

        # act
        instance = OpenThesaurusDb(host="localhost", user="dummy", passwd="dummy", db_name="dummy_db")
        synonyms = instance.get_synonyms(word=word, form='sadsa')

        # assert
        self.assertRaises(RuntimeError)
        self.assertFalse(synonyms)
