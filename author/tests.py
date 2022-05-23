from django.test import TestCase
from django.urls import reverse

from author.models import Author, Book


class ContactTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Big', last_name='Bob', phone="12354698563", email="example@gmail.com")

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 30)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.first_name}{author.last_name}'
        self.assertEqual(str(author), expected_object_name)

class TestModels(TestCase):
    def test_model_str(self):
        book = Book.objects.create(title="The man in the high castle")
        philip = Author.objects.create(first_name="Philip", last_name="K. Dick", phone="1234856985", email="test@gmail.com")
        self.assertEqual(str(book), "The man in the high castle")
        self.assertEqual(str(philip), "PhilipK. Dick")