from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User

# Create your tests here.
class ReviewCreateTest(APITestCase):
    def setUp(self):
        self.user_data = {'email': 'a.t.alli99u@gmail.com', 'password': 'Dbelddl9$'}
        self.review_data = {'title': 'uno', 'content': 'unittest'}
        self.user = User.objects.create_user('')