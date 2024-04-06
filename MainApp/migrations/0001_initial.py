# Generated by Django 5.0.3 on 2024-03-24 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=30)),
                ('phoneNumber', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=30)),
                ('schoolClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.class')),
            ],
        ),
        migrations.CreateModel(
            name='Attestation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('minimumPercentageFor5', models.IntegerField()),
                ('minimumPercentageFor4', models.IntegerField()),
                ('minimumPercentageFor3', models.IntegerField()),
                ('schoolClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('maxPoint', models.IntegerField()),
                ('attestation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.attestation')),
            ],
        ),
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.student')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.task')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.class')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.teacher')),
            ],
        ),
    ]
