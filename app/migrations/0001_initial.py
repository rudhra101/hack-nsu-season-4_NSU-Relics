# Generated by Django 4.1 on 2022-08-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashEmail', models.CharField(max_length=255, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
