from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
import datetime

from notify.models import Company, Notification, Employee, Service


LOGIN_URL = reverse('login')


def create_sample_user(email='test_e@orgincompany.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


def create_sample_employee(user, company, is_admin=False):
    """Create a sample employee"""
    return Employee.objects.create(employee=user,
                                   company=company,
                                   is_admin=is_admin)


def create_admin_sample_user(email='admin@vinoojacob.com',
                             password='testpass'):
    """Create a sample admin user"""
    sample_admin_user = get_user_model().objects.create_user(email, password)
    sample_admin_user.is_staff = True
    return sample_admin_user


def create_sample_company(admin_user, company_name):
    """Create a sample Origin Company"""
    sample_company = Company.objects.create(
        creator=admin_user,
        company_name=company_name,
    )
    return sample_company


def create_sample_service(service_id, company):
    """Create a sample service"""
    return Service.objects.create(service_id=service_id, company=company,)


def create_sample_notification(creator, company,
                               window_start_date, window_start_time,
                               window_end_date, window_endtime,
                               duration, title, description,
                               destination_company, service):
    notification = Notification.objects.create(
        creator=creator,
        origin_company=company,
        window_start_date=window_start_date,
        window_start_time=window_start_time,
        window_end_date=window_end_date,
        window_end_time=window_endtime,
        duration=duration,
        destination_company=destination_company,
        title=title,
        description=description,
        created_date=datetime.date.today()
    )
    notification.service.add(service)
    return notification


class LoginTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            email='test@test.co.nz',
            password='password123',
            name='Test User'
        )

    def test_user_with_credentials_logged_in(self):
        """Test whether an existing user can login in"""

        payload = {
            'username': 'test@test.co.nz',
            'password': 'password123'
        }
        res = self.client.post(LOGIN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'dashboard.html')

    def test_user_with_wrong_password_does_not_login(self):
        """Test that user with a wrong password cannot login"""

        payload = {
            'username': 'test@test.co.nz',
            'password': 'wrongpassword'
        }
        res = self.client.post(LOGIN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'login.html')

    def test_user_without_credentials_fail_to_login(self):
        """Test that a user with in valid credentials does not login"""

        payload = {
            'username': 'fake@fake.com',
            'password': 'wrongpassword'
        }
        res = self.client.post(LOGIN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'login.html')


class ViewQueryTests(TestCase):
    """Test the queries for dashboard views"""

    def setUp(self):
        admin_user1 = create_admin_sample_user(
            email='admin@vocus.com', password='testpass')
        user1 = create_sample_user('user@vocus.com', 'testpass')
        company1 = create_sample_company(admin_user1, 'Vocus')
        create_sample_employee(user1, company1)
        admin_employee1 = create_sample_employee(admin_user1, company1)

        admin_user2 = create_admin_sample_user('admin@spark.com', 'testpass')
        user2 = create_sample_user('user@spark.com', 'testpass')
        company2 = create_sample_company(admin_user2, 'Spark')
        create_sample_employee(user2, company2)
        admin_employee2 = create_sample_employee(admin_user2, company2)
        sample_service = create_sample_service("A35343", company2)
        sample_service2 = create_sample_service("G334343", company2)
        sample_service3 = create_sample_service("NTERS34", company1)

        create_sample_notification(admin_employee1,
                                   company1,
                                   datetime.date(2020, 12, 23),
                                   datetime.time(16, 30),
                                   datetime.date(2020, 12, 23),
                                   datetime.time(17, 30),
                                   30,
                                   "Fibre relocation",
                                   "Fibre relocation from pit 40050 to pit\
                                40285. Moving fibre from pit 40050 to pit\
                                This is likely to take 15 minutes of\
                                switch time but in case of issues,\
                                it will be rolled back",
                                   company2, sample_service
                                   )

        create_sample_notification(admin_employee1,
                                   company1,
                                   datetime.date(2021, 11, 23),
                                   datetime.time(15, 30),
                                   datetime.date(2020, 12, 23),
                                   datetime.time(18, 30),
                                   60,
                                   "Fibre service",
                                   "Fibre relocation from pit 40050 to pit \
                                40285 but in case of issues, it will be \
                                rolled back",
                                   company2,
                                   sample_service2
                                   )

        create_sample_notification(admin_employee2,
                                   company2,
                                   datetime.date(2021, 12, 3),
                                   datetime.time(23, 30),
                                   datetime.date(2020, 12, 4),
                                   datetime.time(1, 20),
                                   60,
                                   "Router upgrade",
                                   "Upgrade of router software with the\
                                latest update. In case of issues, it\
                                will be rolled back",
                                   company1,
                                   sample_service3
                                   )

    def test_outgoing_notification_query(self):
        """Test that all notifications are correctly returned"""

        user1 = get_user_model().objects.get(email='user@vocus.com')
        user2 = get_user_model().objects.get(email='user@spark.com')
        list_notifications_1 = Notification.get_outgoing_notifications(user1)
        list_notifications_2 = Notification.get_outgoing_notifications(user2)
        self.assertEqual(list_notifications_1.count(), 2)
        self.assertEqual(list_notifications_2.count(), 1)

    def test_incoming_notification_query(self):
        """Test that all incoming notifications are queried"""

        user1 = get_user_model().objects.get(email='user@vocus.com')
        user2 = get_user_model().objects.get(email='user@spark.com')
        list_notifications_1 = Notification.get_incoming_notifications(user1)
        list_notifications_2 = Notification.get_incoming_notifications(user2)
        self.assertEqual(list_notifications_1.count(), 1)
        self.assertEqual(list_notifications_2.count(), 2)
