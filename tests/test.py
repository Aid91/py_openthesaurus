import unittest

from py_openthesaurus import OpenThesaurus


class OpenThesaurusTest(unittest.TestCase):

    def test_entry_word_valid_german(self):
        # arrange
        word = 'München'

        # act
        instance = OpenThesaurus(word=word)
        valid = instance.is_entry_word_valid()

        # assert
        self.assertTrue(valid)

    def test_entry_word_not_valid_none(self):
        # arrange
        word = None

        # act
        instance = OpenThesaurus(word=word)
        valid = instance.is_entry_word_valid()

        # assert
        self.assertFalse(valid)

    def test_entry_word_not_valid_all_special_charaters(self):
        # arrange
        word = '!!!$!!!"??'

        # act
        instance = OpenThesaurus(word=word)
        valid = instance.is_entry_word_valid()

        # assert
        self.assertFalse(valid)

    def test_entry_word_not_valid(self):
        # arrange
        word = ''

        # act
        instance = OpenThesaurus(word=word)
        valid = instance.is_entry_word_valid()

        # assert
        self.assertFalse(valid)

    def test_entry_word_valid_special_characters(self):
        # arrange
        word = 'Taking!"WDSDA sadsad!!!'

        # act
        instance = OpenThesaurus(word=word)
        valid = instance.is_entry_word_valid()

        # assert
        self.assertTrue(valid)

    def test_entry_word_valid(self):
        # arrange
        word = 'Taking'

        # act
        instance = OpenThesaurus(word=word)
        valid = instance.is_entry_word_valid()

        # assert
        self.assertTrue(valid)

    def test_get_synonyms_empty_no_word_in_dictionary(self):
        # arrange
        word = 'Taking'

        # act
        instance = OpenThesaurus(word=word)
        synonyms = instance.get_synonyms()

        # assert
        self.assertFalse(synonyms)

    def test_get_synonyms_empty_wrong_input_word(self):
        # arrange
        word = ''

        # act
        instance = OpenThesaurus(word=word)
        synonyms = instance.get_synonyms()

        # assert
        self.assertFalse(synonyms)

    def test_get_synonyms_empty_wrong_input_word_special_characters(self):
        # arrange
        word = None

        # act
        instance = OpenThesaurus(word=word)
        synonyms = instance.get_synonyms()

        # assert
        self.assertFalse(synonyms)

    def test_get_synonyms_full_not_empty(self):
        # arrange
        word = 'gehen'

        # act
        instance = OpenThesaurus(word=word)
        synonyms = instance.get_synonyms(type='full')

        # assert
        self.assertTrue(synonyms)

    def test_get_synonyms_part_not_empty(self):
        # arrange
        word = 'gehen'

        # act
        instance = OpenThesaurus(word=word)
        synonyms = instance.get_synonyms()

        # assert
        self.assertTrue(synonyms)

    def test_get_synonyms_full_part_less(self):
        # arrange
        word = 'gehen'

        # act
        instance = OpenThesaurus(word=word)
        synonyms_part = instance.get_synonyms()
        synonyms_full = instance.get_synonyms(type='full')

        # assert
        synonyms_full_len = len(".".join(synonyms_full))
        synonyms_part_len = len(".".join(synonyms_part))

        self.assertLessEqual(synonyms_part_len, synonyms_full_len)

    def test_get_synonyms_full_part_equal(self):
        # arrange
        word = 'München'

        # act
        instance = OpenThesaurus(word=word)
        synonyms_part = instance.get_synonyms()
        synonyms_full = instance.get_synonyms(type='full')

        # assert
        synonyms_full_len = len(".".join(synonyms_full))
        synonyms_part_len = len(".".join(synonyms_part))

        self.assertLessEqual(synonyms_part_len, synonyms_full_len)

    def test_runtime_error_wrong_type(self):
        # arrange
        word = 'München'

        # act
        instance = OpenThesaurus(word=word)
        synonyms = instance.get_synonyms(type='sadsa')

        # assert
        self.assertRaises(RuntimeError)
        self.assertFalse(synonyms)
