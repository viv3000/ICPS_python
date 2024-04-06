# Generated by Django 4.2.11 on 2024-03-25 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0028_remove_attestation_task_task_attestation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='attestation',
        ),
        migrations.AddField(
            model_name='attestation',
            name='task',
            field=models.ManyToManyField(blank=True, null=True, to='MainApp.task', verbose_name='Задания'),
        ),
    ]