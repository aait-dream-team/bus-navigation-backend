# Generated by Django 4.1.7 on 2023-03-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_alter_admin_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
