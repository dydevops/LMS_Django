# Generated by Django 4.0 on 2022-12-05 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_course_certificate_course_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='certificate',
            field=models.BooleanField(default=False),
        ),
    ]