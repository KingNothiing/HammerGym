from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils.html import escape

from .content import HERO_HIGHLIGHTS
from .models import ContactRequest


@override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    ADMIN_NOTIFICATION_EMAIL='admin@hammergym.com',
    DEFAULT_FROM_EMAIL='HAMMER GYM <no-reply@hammergym.com>',
    SECURE_SSL_REDIRECT=False,
)
class GymViewsTests(TestCase):
    def test_home_page_renders_real_sections(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'HAMMER GYM — тренируйся стабильно, без лишних сложностей')
        self.assertContains(response, 'Тирасполь, ул. Ларионова')
        self.assertContains(response, 'Оскар на Балке')
        self.assertContains(response, 'Стоимость')
        self.assertContains(response, 'Оставить заявку')
        self.assertContains(response, 'Прайс на сайте')
        self.assertContains(response, 'aria-label="Быстрые действия"', html=False)
        self.assertContains(response, escape(HERO_HIGHLIGHTS[0]), html=False)
        self.assertContains(response, 'name="full_name"', html=False)
        self.assertContains(response, 'name="phone"', html=False)
        self.assertIn('locations', response.context)

    def test_submit_contact_request_creates_record_and_sends_email(self):
        response = self.client.post(
            reverse('submit_contact_request'),
            {
                'full_name': 'Ivan Petrov',
                'phone': '+373 777 12 345',
                'branch': 'larionova',
                'message': 'Хочу узнать про абонемент на месяц.',
            },
        )

        self.assertRedirects(response, f"{reverse('home')}#contact")
        self.assertEqual(ContactRequest.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Новая заявка с сайта HAMMER GYM', mail.outbox[0].subject)

    def test_submit_contact_request_with_invalid_payload_returns_home(self):
        response = self.client.post(
            reverse('submit_contact_request'),
            {
                'full_name': '1',
                'phone': '123',
                'branch': 'larionova',
                'message': '',
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(ContactRequest.objects.count(), 0)
        self.assertContains(
            response,
            'Проверьте форму и попробуйте еще раз.',
            status_code=400,
        )
        self.assertIn('locations', response.context)

    def test_health_check_returns_ok_payload(self):
        response = self.client.get(reverse('health_check'))

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {'status': 'ok', 'service': 'hammergym'},
        )


@override_settings(SECURE_SSL_REDIRECT=True)
class GymProductionSecurityTests(TestCase):
    def test_home_redirects_to_https_when_ssl_redirect_enabled(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.headers['Location'], 'https://testserver/')
