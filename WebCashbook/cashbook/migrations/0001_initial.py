# Generated by Django 3.0.8 on 2020-07-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=64)),
                ('password', models.TextField(default='', max_length=30)),
                ('token_value', models.TextField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('creat_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
