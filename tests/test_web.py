import unittest

from py_openthesaurus import OpenThesaurusWeb


class OpenThesaurusWebTest(unittest.TestCase):

    def test_entry_word_valid_german(self):
        # arrange
        word = 'München'

        # act
        instance = OpenThesaurusWeb()
        valid = instance.is_entry_word_valid(word=word)

        # assert
        self.assertTrue(valid)

    def test_entry_word_not_valid_none(self):
        # arrange
        word = None

        # act
        instance = OpenThesaurusWeb()
        valid = instance.is_entry_word_valid(word=word)

        # assert
        self.assertFalse(valid)

    def test_entry_word_not_valid_all_special_charaters(self):
        # arrange
        word = '!!!$!!!"??'

        # act
        instance = OpenThesaurusWeb()
        valid = instance.is_entry_word_valid(word=word)

        # assert
        self.assertFalse(valid)

    def test_entry_word_not_valid(self):
        # arrange
        word = ''

        # act
        instance = OpenThesaurusWeb()
        valid = instance.is_entry_word_valid(word=word)

        # assert
        self.assertFalse(valid)

    def test_entry_word_valid_special_characters(self):
        # arrange
        word = 'Taking!"WDSDA sadsad!!!'

        # act
        instance = OpenThesaurusWeb()
        valid = instance.is_entry_word_valid(word=word)

        # assert
        self.assertTrue(valid)

    def test_entry_word_valid(self):
        # arrange
        word = 'Taking'

        # act
        instance = OpenThesaurusWeb()
        valid = instance.is_entry_word_valid(word=word)

        # assert
        self.assertTrue(valid)

    def test_get_synonyms_empty_no_word_in_dictionary(self):
        # arrange
        word = 'Taking'

        # act
        instance = OpenThesaurusWeb()
        synonyms = instance.get_synonyms(word=word)

        # assert
        self.assertFalse(synonyms)

    def test_get_synonyms_empty_wrong_input_word(self):
        # arrange
        word = ''

        # act
        instance = OpenThesaurusWeb()
        synonyms = instance.get_synonyms(word=word)

        # assert
        self.assertFalse(synonyms)

    def test_get_synonyms_empty_wrong_input_word_special_characters(self):
        # arrange
        word = None

        # act
        instance = OpenThesaurusWeb()
        synonyms = instance.get_synonyms(word=word)

        # assert
        self.assertFalse(synonyms)

    def test_get_synonyms_long_not_empty(self):
        # arrange
        word = 'gehen'

        # act
        instance = OpenThesaurusWeb()
        synonyms = instance.get_synonyms(word=word, form='long')

        # assert
        self.assertTrue(synonyms)

    def test_get_synonyms_short_not_empty(self):
        # arrange
        word = 'gehen'

        # act
        instance = OpenThesaurusWeb()
        synonyms = instance.get_synonyms(word=word)

        # assert
        self.assertTrue(synonyms)

    def test_get_synonyms_long_short(self):
        # arrange
        word = 'gehen'

        # act
        instance = OpenThesaurusWeb()
        synonyms_short = instance.get_synonyms(word=word)
        synonyms_long = instance.get_synonyms(word=word, form='long')

        # assert
        synonyms_long_len = len(".".join(synonyms_long))
        synonyms_short_len = len(".".join(synonyms_short))

        self.assertLessEqual(synonyms_short_len, synonyms_long_len)

    def test_get_synonyms_long_short_equal(self):
        # arrange
        word = 'München'

        # act
        instance = OpenThesaurusWeb()
        synonyms_short = instance.get_synonyms(word=word)
        synonyms_long = instance.get_synonyms(word=word, form='long')

        # assert
        synonyms_long_len = len(".".join(synonyms_long))
        synonyms_short_len = len(".".join(synonyms_short))

        self.assertLessEqual(synonyms_short_len, synonyms_long_len)

    def test_runtime_error_wrong_type(self):
        # arrange
        word = 'München'

        # act
        instance = OpenThesaurusWeb()
        synonyms = instance.get_synonyms(word=word, form='sadsa')

        # assert
        self.assertRaises(RuntimeError)
        self.assertFalse(synonyms)
