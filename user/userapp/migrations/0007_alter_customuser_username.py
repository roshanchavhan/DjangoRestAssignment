# Generated by Django 4.1.5 on 2023-01-31 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, default=['q'], max_length=255, verbose_name='User_name'),
        ),
    ]