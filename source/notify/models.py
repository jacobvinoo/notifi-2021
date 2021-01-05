from django.db import models
from django.conf import settings


class Company(models.Model):
    """Company for the notification"""
    company_name = models.CharField(max_length=255)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.company_name


class Employee(models.Model):
    """Employee model"""
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    company = models.ForeignKey(Company,
                                blank=True,
                                null=True,
                                on_delete=models.SET_NULL)
    is_admin = models.BooleanField(blank=True)

    def __str__(self):
        return self.employee.email


class Service(models.Model):
    """Services associated with each notification"""

    service_id = models.CharField(max_length=50)
    company = models.ForeignKey(Company,
                                blank=True,
                                null=True,
                                on_delete=models.SET_NULL)

    def __str__(self):
        return self.service_id


class Notification(models.Model):
    """Notification model """
    creator = models.ForeignKey(Employee,
                                blank=True,
                                null=True,
                                on_delete=models.SET_NULL)
    origin_company = models.ForeignKey(Company,
                                       blank=True,
                                       null=True,
                                       on_delete=models.SET_NULL)
    window_start_date = models.DateField()
    window_start_time = models.TimeField()
    window_end_date = models.DateField()
    window_end_time = models.TimeField()
    duration = models.IntegerField()
    title = models.TextField()
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    destination_company = models.ForeignKey(Company,
                                            blank=True,
                                            null=True,
                                            on_delete=models.SET_NULL,
                                            related_name="destination")
    service = models.ForeignKey(Service,
                                blank=True,
                                null=True,
                                on_delete=models.SET_NULL)

    def get_list_of_notifications(user):
        employee = Employee.objects.get(employee=user)
        company = Company.objects.get(company_name=employee.company)
        return Notification.objects.filter(origin_company=company)

    def __str__(self):
        return self.title
