# Generated by Django 3.0.6 on 2020-07-28 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.CharField(editable=False, max_length=200, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]