# Generated by Django 2.2.1 on 2019-06-14 10:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
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
                ('name', models.CharField(max_length=128, unique=True, validators=[django.core.validators.MaxLengthValidator(128)])),
                ('attributes', models.CharField(max_length=256, validators=[service.validators.validate_json, django.core.validators.MaxLengthValidator(256)])),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json_content', models.CharField(max_length=16384, validators=[service.validators.validate_task_json_content, django.core.validators.MaxLengthValidator(16384)])),
                ('status', models.CharField(default='pending', max_length=16, validators=[django.core.validators.MaxLengthValidator(16)])),
                ('task_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('msg', models.CharField(blank=True, default=None, max_length=512, null=True, validators=[django.core.validators.MaxLengthValidator(512)])),
                ('bytes', models.IntegerField(blank=True, default=None, null=True)),
                ('data_set', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='service.DataSet', validators=[service.validators.validate_data_set])),
            ],
        ),
    ]
