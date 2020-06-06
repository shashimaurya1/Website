from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Inseration
from account.models import Account

import os


class CreateAccountTest(TestCase):

    def setUp(self):
        self.user = Account.objects.create_user('user@mail.com', 'user', 'pwd', 'title', 'first', 'last', 'street',
                                                '1', '12345', 'city', 'de')
        self.image = SimpleUploadedFile(name='bla.jpg', content=open('marketplace/static/assets/img/nophoto.jpg', 'rb').read(), content_type='image/jpeg')
        #self.inseration = Inseration.objects.create_inseration('title', 'description', self.image, 'Top', 'T-Shirt', '3XL', inserter=self.user)
        self.inseration = Inseration.objects.create(title='title', description='description', images=self.image, category='Top', subcategory='T-Shirt', size='3XL', inserter=self.user)

    def testBasic(self):
        self.assertEqual(self.inseration.title, 'title')
        self.assertEqual(self.inseration.description, 'description')
        self.assertEqual(self.inseration.images, 'images/bla.jpg')
        self.assertEqual(self.inseration.category, 'Top')
        self.assertEqual(self.inseration.subcategory, 'T-Shirt')
        self.assertEqual(self.inseration.size, '3XL')

    def tearDown(self):
        os.remove('media/images/bla.jpg',)
