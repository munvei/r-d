# Generated by Django 3.1.2 on 2020-11-22 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=100)),
                ('task_id', models.CharField(max_length=100)),
                ('next_task', models.CharField(max_length=100)),
                ('next_url', models.CharField(max_length=100)),
            ],
        ),
    ]
