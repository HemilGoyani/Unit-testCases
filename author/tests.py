from django.test import TestCase
from django.urls import reverse

from .models import Author


class ContactTests(TestCase):

   def setUp(self):
       Author.objects.create(
           first_name='Ousseynou',
           last_name="Diop",
           phone="779929900",
           email="hello@me.com"
       )

   def test_email_content(self):
       contact = Author.objects.get(id=1)
       expected_object_name = f'{contact.email}'
       self.assertEquals(expected_object_name, 'hello@me.com')

   def test_contact_list_view(self):
       response = self.client.get(reverse('contacts'))
       self.assertEqual(response.status_code, 200)
       self.assertContains(response, 'hello@me.com')
       self.assertTemplateUsed(response, 'pages/author.html')