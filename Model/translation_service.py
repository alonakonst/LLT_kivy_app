"""
Translation Service
Usage:
    >> translation_service = TranslationService('/path/to/credential/file.json')
    >> translate('hus')
    house
"""

import requests


class TranslationServiceError(Exception):
    pass


class TranslationService:
    """
    Google Translation API client, initialise and use the 'translate' method
    :param: credentials_path: The path to the service account credentials in json format
    :type credentials_path: str
    :param source_language: The source language used in all translation api calls, defaults to 'da' (Danish)
    :type source_language: str
    :param target_language: The target language used in all translation api calls, defaults to 'en' (English)
    :type target_language: str
    :raises TranslationServiceError: If there is an error when authenticating
    """

    BASE_URL = 'https://translation.googleapis.com/language/translate/v2'

    def __init__(self,
                 api_key: str,
                 *, source_language: str = 'da', target_language: str = 'en', maximum_text_length=128):

        self.api_key = api_key
        self.source_language = source_language
        self.target_language = target_language
        self.maximum_text_length = maximum_text_length

    def translate(self, text: str) -> str:
        """
        This returns a string with the most likely translation of text using the Google Translation API
        :param text: The text to be translated
        :type text: str
        :return: The translation of the text
        :rtype: str
        :raise ValueError: If the text is not a str, empty, or too long
        :raise TranslationServiceError: If there is a Google API error or any other error when making the request
        """
        # check if the text is valid
        if not text or not isinstance(text, str):
            raise ValueError("Invalid text provided for translation.")

        if len(text) > self.maximum_text_length:
            raise ValueError(f"text must have at most {self.maximum_text_length}, not {len(text)}.")

        try:
            res = requests.post(self.BASE_URL, params={
                'q': text,
                'source': self.source_language,
                'target': self.target_language,
                'key': self.api_key,
            })

            translation = res.json()['data']['translations'][0]['translatedText']

            return translation

        except Exception as e:
            raise TranslationServiceError(f"Error while translating '{text}': {e}") from e
