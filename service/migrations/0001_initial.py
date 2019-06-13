# Generated by Django 2.2.1 on 2019-06-13 13:36

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import service.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_set', models.CharField(max_length=128, unique=True)),
                ('attributes', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('json_content', models.CharField(max_length=16384, validators=[service.validators.validate_json_content, django.core.validators.MaxLengthValidator(16384)])),
                ('status', models.CharField(default='pending', max_length=16, validators=[django.core.validators.MaxLengthValidator(16)])),
                ('msg', models.CharField(blank=True, default='', max_length=512, validators=[django.core.validators.MaxLengthValidator(512)])),
                ('bytes', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
