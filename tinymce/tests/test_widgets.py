# coding: utf-8

from django.test import TestCase, override_settings

from tinymce.widgets import get_language_config


@override_settings(LANGUAGES=[('en', 'English')])
class TestWidgets(TestCase):

    def test_default_config(self):
        config = get_language_config()
        config_ok = {
            'spellchecker_languages': '+English=en',
            'directionality': 'ltr',
            'language': 'en',
            'spellchecker_rpc_url': '/tinymce/spellchecker/'
        }
        self.assertEqual(config, config_ok)

    @override_settings(LANGUAGES_BIDI=['en'])
    def test_default_config_rtl(self):
        config = get_language_config()
        config_ok = {
            'spellchecker_languages': '+English=en',
            'directionality': 'rtl',
            'language': 'en',
            'spellchecker_rpc_url': '/tinymce/spellchecker/'
        }
        self.assertEqual(config, config_ok)

    def test_content_language(self):
        config = get_language_config('ru-ru')
        config_ok = {
            'spellchecker_languages': 'English=en',
            'directionality': 'ltr',
            'language': 'en',
            'spellchecker_rpc_url': '/tinymce/spellchecker/'
        }
        self.assertEqual(config, config_ok)

    def test_tinymce_widget(self):
        # TODO: implement test
        pass
