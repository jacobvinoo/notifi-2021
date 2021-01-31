from django.test import TestCase
from django.contrib.auth import get_user_model
import datetime

from notify import models


def create_admin_sample_user(email='admin@vinoojacob.com',
                             password='testpass'):
    """Create a sample admin user"""
    sample_admin_user = get_user_model().objects.create_user(email, password)
    sample_admin_user.is_staff = True
    return sample_admin_user


def create_sample_user(email='test_e@orgincompany.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


def create_sample_company(user, company_name='Origin Company'):
    """Create a sample Origin Company"""
    sample_company = models.Company.objects.create(
        creator=user,
        company_name=company_name,
    )
    return sample_company


def create_sample_employee(user, company, is_admin=False):
    """Create a sample employee"""
    return models.Employee.objects.create(employee=user,
                                          company=company,
                                          is_admin=is_admin)


def create_sample_service(service_id, company):
    """Create a sample service"""
    return models.Service.objects.create(service_id=service_id,
                                         company=company,)


def create_sample_notifications():
    sample_user1 = create_sample_user()
    sample_company = create_sample_company(sample_user1, "Vocus")
    sample_company2 = create_sample_company(sample_user1, "Spark")
    sample_employee = create_sample_employee(sample_user1, sample_company)
    sample_service = create_sample_service("A35343", sample_company2)
    sample_service1 = create_sample_service("A73433", sample_company2)

    notification1 = models.Notification.objects.create(
        creator=sample_employee,
        origin_company=sample_company,
        window_start_date=datetime.date(2020, 12, 23),
        window_start_time=datetime.time(15, 30),
        window_end_date=datetime.date(2020, 12, 23),
        window_end_time=datetime.time(16, 30),
        duration=30,
        destination_company=sample_company2,
        title="Fibre relocation from pit 40050 to pit 40285",
        description="Moving fibre from pit 40050 to pit 40285.\
                        This is likely to take 15 minutes of switch time\
                        but in case of issues, it will be rolled back",
        created_date=datetime.date.today()
    )
    notification1.service.add(sample_service)

    notification2 = models.Notification.objects.create(
        creator=sample_employee,
        origin_company=sample_company2,
        window_start_date=datetime.date(2020, 12, 23),
        window_start_time=datetime.time(15, 30),
        window_end_date=datetime.date(2020, 12, 23),
        window_end_time=datetime.time(16, 30),
        duration=30,
        destination_company=sample_company,
        title="Fibre relocation from pit ",
        description="Moving fibre from pit 40050 to pit 40285.\
                        This is likely to take 15 minutes of switch time\
                        but in case of issues, it will be rolled back",
        created_date=datetime.date.today()
    )
    notification2.service.add(sample_service1)

    notifications = [notification1, notification2]
    return notifications


class ModelTests(TestCase):

    def test_company_str(self):
        """Test that company string representation"""
        company = models.Company.objects.create(
            creator=create_admin_sample_user(),
            company_name='Vocus',
        )

        self.assertEqual(str(company), company.company_name)

    def test_notification_str(self):
        """Test the notification string representation"""
        notifications = create_sample_notifications()
        notification = notifications[0]

        self.assertEqual(str(notification), notification.title)

    def test_employee_str(self):
        """Test the employee can be created and string represented"""

        user1 = create_sample_user('user@vocus.com', 'testpass')
        company = create_sample_company(user1, company_name="Vocus")

        employee = models.Employee.objects.create(
            employee=user1,
            company=company,
            is_admin=False
        )

        self.assertEqual(str(employee), 'user@vocus.com')

    def test_work_str(self):
        """Test the work can be created and string represented"""

        notifications = create_sample_notifications()
        notification1 = notifications[0]
        notification2 = notifications[1]

        work1 = models.Work.objects.create(
            title="Router Software Upgrade"
        )
        work1.notification.add(notification1)
        work1.notification.add(notification2)

        self.assertEqual(str(work1), "Router Software Upgrade")
        self.assertEqual(work1.notification.count(), 2)
