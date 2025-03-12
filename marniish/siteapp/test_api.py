"""Тесты полностью сгенерировал с помощью DeepSeek,
правда создавал промт 2 дня, в общей сложности ушло около часа"""
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from mixer.backend.django import mixer

User = get_user_model()


class PermissionTests(APITestCase):
    def setUp(self):
        self.user = mixer.blend(User, is_superuser=False)
        self.superuser = mixer.blend(User, is_superuser=True)

        self.article = mixer.blend('siteapp.Article')
        self.page = mixer.blend('siteapp.Page')
        self.trend = mixer.blend('siteapp.Trend')
        self.trend_item = mixer.blend('siteapp.TrendItem')
        self.news = mixer.blend('siteapp.News')

    def test_article_read_only(self):
        """
        Проверка, что неаутентифицированные пользователи могут читать статьи, но не могут их изменять.
        """
        url = reverse('article-detail', args=[self.article.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.put(url, {})  # Попытка изменить статью
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_page_admin_or_read_only(self):
        """
        Проверка, что страницы могут читать неаутентифицированные пользователи,
        и изменять только суперпользователи.
        """
        url = reverse('page-detail', args=[self.page.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, {})  # Попытка изменить страницу обычным пользователем
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_trend_item_admin_or_read_only(self):
        """
        Аналогично test_page_admin_or_read_only, но для TrendItem.
        """
        url = reverse('trenditem-detail', args=[self.trend_item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_news_read_only(self):
        """
        Проверка, что неаутентифицированные пользователи могут читать новости, но не могут их изменять.
        """
        url = reverse('news-detail', args=[self.news.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.put(url, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_siteuser_admin_or_read_only(self):
        """Проверка, что обычный пользователь может прочитать список пользователей,
        но не может их изменять, а суперпользователь может всё.
        """
        url = reverse('siteuser-list')

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.put(reverse('siteuser-detail', args=[self.user.id]), {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)