# Generated by Django 5.0.3 on 2024-03-25 00:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0018_remove_attestation_task_task_attestation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='attestation',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата проведения'),
        ),
        migrations.AlterField(
            model_name='attestation',
            name='minimumPercentageFor3',
            field=models.IntegerField(blank=True, null=True, verbose_name='% для 3'),
        ),
        migrations.AlterField(
            model_name='attestation',
            name='minimumPercentageFor4',
            field=models.IntegerField(blank=True, null=True, verbose_name='% для 4'),
        ),
        migrations.AlterField(
            model_name='attestation',
            name='minimumPercentageFor5',
            field=models.IntegerField(blank=True, null=True, verbose_name='% для 5'),
        ),
        migrations.AlterField(
            model_name='attestation',
            name='schoolClass',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.schoolclass', verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='attestation',
            name='subject',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.subject', verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='attestation',
            name='teacher',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.teacher', verbose_name='Учитель'),
        ),
        migrations.AlterField(
            model_name='attestation',
            name='theme',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='attestation',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='schoolclass',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Буква класса'),
        ),
        migrations.AlterField(
            model_name='schoolclass',
            name='year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Год набора'),
        ),
        migrations.AlterField(
            model_name='student',
            name='fullName',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='student',
            name='results',
            field=models.ManyToManyField(blank=True, to='MainApp.taskresult', verbose_name='Результаты заданий'),
        ),
        migrations.AlterField(
            model_name='student',
            name='schoolClass',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='MainApp.schoolclass', verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='attestation',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.attestation', verbose_name='Учитель'),
        ),
        migrations.AlterField(
            model_name='task',
            name='maxPoint',
            field=models.IntegerField(blank=True, null=True, verbose_name='Максимальный балл'),
        ),
        migrations.AlterField(
            model_name='task',
            name='skill',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Проверяемый навык'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='taskresult',
            name='point',
            field=models.IntegerField(blank=True, null=True, verbose_name='Баллы'),
        ),
        migrations.AlterField(
            model_name='taskresult',
            name='task',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.task', verbose_name='Задание'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='classes',
            field=models.ManyToManyField(blank=True, to='MainApp.schoolclass', verbose_name='Классы'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='fullName',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефонный номер'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.ManyToManyField(blank=True, to='MainApp.subject', verbose_name='Предметы'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]