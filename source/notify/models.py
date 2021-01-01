from django.db import models
from django.conf import settings

from core.models import User


class Company(models.Model):
    """Company for the notification"""
    company_name = models.CharField(max_length=255)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    admin_person = models.ForeignKey(User,
                                     related_name='company_admin',
                                     on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.company_name


class Notification(models.Model):
    """Notification model """
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    orgin_company = models.ForeignKey(Company,
                                      on_delete=models.CASCADE)
    date_of_outage = models.DateField()
    window_start_time = models.TimeField()
    window_end_time = models.TimeField()
    duration = models.IntegerField()
    title = models.TextField()
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    service_id = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    """Employee model"""
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.employee.email
