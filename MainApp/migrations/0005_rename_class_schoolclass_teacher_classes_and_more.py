# Generated by Django 5.0.3 on 2024-03-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_alter_attestation_theme_alter_attestation_type_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Class',
            new_name='SchoolClass',
        ),
        migrations.AddField(
            model_name='teacher',
            name='classes',
            field=models.ManyToManyField(to='MainApp.schoolclass'),
        ),
        migrations.DeleteModel(
            name='ClassList',
        ),
    ]
