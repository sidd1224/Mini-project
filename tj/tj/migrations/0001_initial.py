# Generated by Django 5.1.2 on 2024-12-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('username', models.CharField(max_length=150, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
