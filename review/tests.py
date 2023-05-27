from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User



class ReviewCreateTest(APITestCase):
    #     self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']
    @classmethod    
    def setUpTestData(cls):
        cls.user_data = {'email': 'unity@ty.ty', 'password': 'universe'}
        cls.review_data = {'title': 'yunityday', 'content': 'unittest'}
        cls.user = User.objects.create_user('unity@ty.ty', 'universe')
        
    def setUp(self):
        self.url = reverse('')
        
    def test_fail_if_not_logged_in(self):
        url = reverse("review_view")
        response = self.client.post(url, self.review_data)
        self.assertEqual(response.status_code, 401)
        
    # def test_create_review(self):
    #     response = self.client.post(
    #         path=reverse("review_view"),
    #         data=self.review_data,
    #         HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
    #     )
    #     self.assertEqual(response.data["message"], "글 작성 완료-옷!")
        