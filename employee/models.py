from django.db import models
from django.core.validators import RegexValidator


class Employee(models.Model):
  name = models.CharField(max_length=100)
  address = models.TextField()
  phone_number = models.CharField(
      max_length=15,
      validators=[RegexValidator(r'^\d+$', 'Phone number must be numeric')])
  salary = models.DecimalField(max_digits=10, decimal_places=2)
  designation = models.CharField(max_length=100)
  short_description = models.TextField()

  def __str__(self):
    return self.name
