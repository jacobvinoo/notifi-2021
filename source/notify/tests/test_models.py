from django.test import TestCase
from django.contrib.auth import get_user_model
import datetime

from notify import models


def admin_sample_user(email='admin@vinoojacob.com', password='testpass'):
    """Create a sample admin user"""
    sample_admin_user = get_user_model().objects.create_user(email, password)
    sample_admin_user.is_staff = True
    return sample_admin_user


def sample_user(email='test_e@orgincompany.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


def sample_user_1(email='test1@orgincompany.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


def sample_orgin_company(company_name='Origin Company'):
    """Create a sample Origin Company"""
    sample_company = models.Company.objects.create(
        creator=sample_user('test2@origincompany.com', 'testpass'),
        company_name=company_name,
        admin_person=admin_sample_user()
    )
    return sample_company


class ModelTests(TestCase):

    def test_company_str(self):
        """Test that company string representation"""
        company = models.Company.objects.create(
            creator=admin_sample_user(),
            company_name='Vocus',
            admin_person=sample_user(),
        )

        self.assertEqual(str(company), company.company_name)

    def test_notification_str(self):
        """Test the notification string representation"""

        notification = models.Notification.objects.create(
            creator=sample_user(),
            orgin_company=models.Company.objects.create(
                creator=admin_sample_user(),
                company_name='Vocus',
                admin_person=sample_user_1()),
            date_of_outage=datetime.date(2020, 12, 23),
            window_start_time=datetime.time(15, 30),
            window_end_time=datetime.time(16, 30),
            duration=30,
            title="Fibre relocation from pit 40050 to pit 40285",
            description="Moving fibre from pit 40050 to pit 40285.\
                            This is likely to take 15 minutes of switch time\
                            but in case of issues, it will be rolled back",
            service_id='A15434',
            created_date=datetime.date.today()
        )

        self.assertEqual(str(notification), notification.title)

    def test_employee_str(self):
        """Test the employee can be created and string represented"""

        employee = models.Employee.objects.create(
            employee=sample_user(),
            company=sample_orgin_company(company_name="Company1")
        )

        self.assertEqual(str(employee), 'test_e@orgincompany.com')
