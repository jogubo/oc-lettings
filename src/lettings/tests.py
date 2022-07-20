from faker import Faker

from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class LettingTest(TestCase):

    faker = Faker()

    def setUp(self):
        self.address = Address.objects.create(
            number=self.faker.random_int(min=1, max=9999),
            street=self.faker.street_name(),
            city=self.faker.city(),
            state=self.faker.state(),
            zip_code=self.faker.random_int(min=1, max=99999),
            country_iso_code=self.faker.country_code(),
        )

        self.letting = Letting.objects.create(
            title='SampleAddress',
            address=self.address,
        )

    def test_index_page(self):
        response = self.client.get(reverse('lettings_index'))
        assert response.status_code == 200
        assert b'<title>Lettings</title>' in response.content
        assert self.letting.title.encode('utf-8') in response.content

    def test_letting_page(self):
        response = self.client.get(reverse('letting', args=[self.letting.pk]))
        assert response.status_code == 200
        assert self.letting.title.encode('utf-8') in response.content
        assert self.letting.address.street.encode('utf-8') in response.content
        assert self.letting.address.city.encode('utf-8') in response.content
        assert self.letting.address.state.encode('utf-8') in response.content
