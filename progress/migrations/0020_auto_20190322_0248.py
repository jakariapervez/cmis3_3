# Generated by Django 2.0.3 on 2019-03-21 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0019_auto_20190320_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='dpp_intervention',
            name='contract_status',
            field=models.CharField(blank=True, choices=[('HAVE_CONTRACT', 'HAVE_CONTRACT'), ('HAVE_NO_CONTRACT', 'HAVE_NO_CONTRACT')], default=('HAVE_NO_CONTRACT', 'HAVE_NO_CONTRACT'), max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dpp_intervention',
            name='work_status',
            field=models.CharField(blank=True, choices=[('OG', 'OG'), ('COMP', 'COMP'), ('TO_BE_STARTED', 'TO_BE_STARTED')], default=('TO_BE_STARTED', 'TO_BE_STARTED'), max_length=100, null=True),
        ),
    ]
