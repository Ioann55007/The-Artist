from django.test import TestCase
import unittest
from django.test import Client


class ProfileViewTest(TestCase):

    def test_profile(self):
        response = self.client.get('/profile/6')
        self.assertEqual(response.status_code, 301)


class ProfileUploadTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_profile_upload(self):
        response = self.client.get('/edit/6')
        self.assertEqual(response.status_code, 301)