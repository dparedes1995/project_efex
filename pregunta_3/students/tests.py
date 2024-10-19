from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student

class StudentAPITestCase(APITestCase):

    def setUp(self):
        self.student_1 = Student.objects.create(
            first_name="Scarlett",
            last_name="Evans",
            date_of_birth="2010-05-01",
            grade=8,
            phone="+11111111111",
            email="scarlet@email.com"
        )

    def test_get_students(self):
        url = reverse('student-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['first_name'], "Scarlett")

    def test_post_student(self):
        url = reverse('student-list')
        data = {
            "first_name": "Lily",
            "last_name": "Davies",
            "date_of_birth": "2010-03-15",
            "grade": 8,
            "phone": "+11111112222",
            "email": "lily@email.com"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)

    def test_patch_student(self):
        url = reverse('student-detail', kwargs={'pk': self.student_1.pk})
        data = {
            "grade": 9,
            "phone": "+11111111000"
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student_1.refresh_from_db()
        self.assertEqual(self.student_1.grade, 9)
        self.assertEqual(self.student_1.phone, "+11111111000")

    def test_get_single_student(self):
        url = reverse('student-detail', kwargs={'pk': self.student_1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], "Scarlett")
