# Generated by Django 4.2.1 on 2023-09-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_testmodel_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='username',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
