from django.db import models

# Create your models here.
class Account(models.Model):
    account_name = models.CharField(max_length=64)
    account_password = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account_name
