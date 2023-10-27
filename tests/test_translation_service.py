import unittest

from Model import TranslationService


class TranslationServiceTestCase(unittest.TestCase):
    def test_data_validation(self):
        translation_service = TranslationService('credentials.json', maximum_text_length=2)

        with self.assertRaises(ValueError):
            translation_service.translate(None)

        with self.assertRaises(ValueError):
            translation_service.translate('')

        with self.assertRaises(ValueError):
            translation_service.translate('123')
