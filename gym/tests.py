from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import ContactRequest


@override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    ADMIN_NOTIFICATION_EMAIL='admin@hammergym.com',
    DEFAULT_FROM_EMAIL='HAMMER GYM <no-reply@hammergym.com>',
)
class GymViewsTests(TestCase):
    def test_home_page_renders_real_sections(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'HAMMER GYM для тех, кто хочет тренироваться стабильно и без лишней сложности')
        self.assertContains(response, 'Тирасполь, ул. Ларионова')
        self.assertContains(response, 'Оскар на Балке')
        self.assertContains(response, 'Стоимость')
        self.assertContains(response, 'Фото зала и атмосферы')
        self.assertContains(response, 'Так будет выглядеть блок с тренерами')
        self.assertContains(response, 'Открыть на карте')
        self.assertIn('locations', response.context)

    def test_submit_contact_request_creates_record_and_sends_email(self):
        response = self.client.post(
            reverse('submit_contact_request'),
            {
                'full_name': 'Ivan Petrov',
                'phone': '111',
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
                'full_name': '',
                'phone': '',
                'branch': 'larionova',
                'message': '',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactRequest.objects.count(), 0)
        self.assertContains(response, 'Проверьте форму и попробуйте еще раз.')
        self.assertIn('locations', response.context)
