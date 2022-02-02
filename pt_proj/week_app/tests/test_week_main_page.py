import datetime

from django.test import TestCase
from django.urls import reverse_lazy


class RestorePasswordTest(TestCase):

    def test_restore_password_url_exists_at_desired_location(self):
        """Тест по ссылке www.site.ru/ при отправке GET запроса код 200"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        """Тест по name url что ссылка возвращает статус код 200
        и то что использует свой шаблон index.html"""
        response = self.client.get(reverse_lazy('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_post_request_date(self):
        """Тестируем при отправке пост запроса с в форму дату 27-01-2019 года для подсчета неделей,
        должен вернуть строку на странице 'Starting from 01.01.2019 to' и статус код=200,
        а так же должно получится 5 недель в тексте должно вернуться '5 weeks'"""
        response = self.client.post(reverse_lazy('main'), {'date': datetime.date(day=27, month=1, year=2019)})
        self.assertContains(response, 'Starting from 01.01.2019 to', status_code=200)
        self.assertContains(response, '5 weeks', status_code=200)

    def test_bad_post_request_data(self):
        """Тестируем при отправке пост запроса с в форму ошибочную дату 07-12-2018 года (так как форма настроена
        для приема даты начиная от 01-01-2019, НЕ должен вернуть строку на странице 'Starting from 01.01.2019 to'
        и статус код=200, а так же должен вернуться статус код=324"""
        response = self.client.post(reverse_lazy('main'), {'date': datetime.date(day=7, month=12, year=2018)})
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 324)
        self.assertNotContains(response, 'Starting from 01.01.2019 to', status_code=324)
