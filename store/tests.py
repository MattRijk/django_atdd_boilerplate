from django.test import TestCase, Client


class TestHomePageView(TestCase):

    def test_homepageview_status_success(self):
        request = Client()
        response = request.get('/')
        self.assertEqual(response.status_code, 200)
