# coding: utf-8

from mock import patch

from django.contrib.flatpages.models import FlatPage
from django.test import TestCase

from tinymce.views import render_to_image_list


class TestViews(TestCase):
    def test_spell_check(self):
        # TODO: implement test for spellchecker
        pass

    def test_flatpages_link_list(self):
        FlatPage.objects.create(
            url='/test/url',
            title='Test Title',
        )
        response = self.client.get('/tinymce/flatpages_link_list/')
        result_ok = b'var tinyMCELinkList = [["Test Title", "/test/url"]];'
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/x-javascript', response['Content-Type'])
        self.assertEqual(result_ok, response.content)

    def test_compressor(self):
        # TODO: implement test
        pass

    def test_render_to_image_list(self):
        response = render_to_image_list([('test', 'test.jpg')])
        result_ok = b'var tinyMCEImageList = [["test", "test.jpg"]];'
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/x-javascript', response['Content-Type'])
        self.assertEqual(result_ok, response.content)

    @patch('tinymce.views.urlresolvers.reverse', return_value='/filebrowser')
    def test_filebrowser(self, reverse_mock):
        response = self.client.get('/tinymce/filebrowser/')
        response_ok = b'function djangoFileBrowser(field_name, url, type, win) {\n    var url = "http://testserver/filebrowser?pop=2&type=" + type;\n\n    tinyMCE.activeEditor.windowManager.open(\n        {\n            \'file\': url,\n            \'width\': 820,\n            \'height\': 500,\n            \'resizable\': "yes",\n            \'scrollbars\': "yes",\n            \'inline\': "no",\n            \'close_previous\': "no"\n        },\n        {\n            \'window\': win,\n            \'input\': field_name,\n            \'editor_id\': tinyMCE.selectedInstance.editorId\n        }\n    );\n    return false;\n}\n'
        self.assertEqual(200, response.status_code)
        self.assertEqual(response_ok, response.content)
