from django.db import models

# Create your models here.
class account(models.Model):
    account_name = models.CharField(max_length=64)
    password = models.TextField(max_length=30, default='')
    token_value = models.TextField(max_length=100)
    status = models.CharField(max_length=100)
    creat_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.account_name
