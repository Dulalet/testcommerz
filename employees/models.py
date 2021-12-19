import uuid as uuid
from django.db import models


class Employee(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=40, blank=False, null=False)
    position = models.TextField(max_length=10, blank=False, null=False)
    employment_date = models.DateField(blank=False, null=False)
    salary = models.IntegerField(blank=False, null=False)
    supervisor = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
