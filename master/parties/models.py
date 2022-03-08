from django.db import models

# Create your models here.

customer_type = [
    ('individual', 'Individual'),
    ('company', 'Company'),
]

class Parties(models.Model):
    name = models.CharField(max_length=200)
    customer_type = models.CharField(choices=customer_type, max_length=144)
    address = models.TextField(null=True, blank=True)
    Tax_ID = models.CharField(max_length=200,null=True, blank=True)
    phone = models.CharField(max_length=25,null=True, blank=True)
    mobile = models.CharField(max_length=25,null=True, blank=True)
    email = models.EmailField(max_length=200,null=True, blank=True)
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name



