# Generated by Django 5.0.6 on 2024-05-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_picture_contact_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
