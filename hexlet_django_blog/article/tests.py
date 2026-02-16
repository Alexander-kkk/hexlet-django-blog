from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class ArticleTest(TestCase):
    def test_users_list(self):
        response = self.client.get(reverse("article_index"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['text'], 'Статьи')


