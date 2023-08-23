# Generated by Django 2.0 on 2023-08-23 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('job_id', models.CharField(max_length=20, unique=True)),
                ('company_name', models.CharField(max_length=255)),
                ('company_location', models.CharField(max_length=255)),
                ('posting_date', models.DateField()),
                ('job_description_url', models.URLField()),
                ('salary', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
    ]
