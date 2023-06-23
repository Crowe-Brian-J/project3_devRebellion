from django.test import TestCase
from django.core import mail
# Create your tests here.
class EmailTest(TestCase):

    def test_send_email(self):
        mail.send_mail(
            'That’s your subject',
            'That’s your message body',
            'from@yurii.com',
            ['to@yourfriend.com'],
            fail_silently=False,
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'That’s your subject')
        self.assertEqual(mail.outbox[0].body, 'That’s your message body')