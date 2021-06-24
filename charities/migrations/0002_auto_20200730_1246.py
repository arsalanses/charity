# Generated by Django 3.0.8 on 2020-07-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charities', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='benefactor',
            old_name='free_time',
            new_name='free_time_per_week',
        ),
        migrations.AlterField(
            model_name='task',
            name='age_limit_from',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='age_limit_to',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='gender_limit',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]