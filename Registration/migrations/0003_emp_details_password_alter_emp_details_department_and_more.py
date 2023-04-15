# Generated by Django 4.2 on 2023-04-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0002_emp_details_delete_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp_details',
            name='password',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emp_details',
            name='department',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='emp_details',
            name='phone_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='emp_details',
            name='role',
            field=models.CharField(max_length=100),
        ),
    ]