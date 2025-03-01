# Generated by Django 5.1.6 on 2025-02-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('DateOfBirth', models.CharField(max_length=100)),
                ('Course', models.CharField(max_length=100)),
                ('EnrollmentDate', models.DateField()),
            ],
        ),
    ]
