# Generated by Django 3.0.3 on 2020-02-07 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inputfile',
            old_name='input',
            new_name='exercise',
        ),
        migrations.RenameField(
            model_name='outputfile',
            old_name='input',
            new_name='exercise',
        ),
    ]
