import unittest

from django.test import TestCase
from django.test import Client
from django.urls import reverse


class ViewIconTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_icon_list(self):
        response = self.client.get('/icons')
        self.assertEqual(response.status_code, 301)



class DetailIconTest(TestCase):
    def test_icon_detail(self):
        response = self.client.get(reverse('icon:icon'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context['icons'], [])



class DetailLikeTest(TestCase):
    def test_icon_detail(self):
        response = self.client.get('icon_like/2')
        self.assertEqual(response.status_code, 200)





