# Generated by Django 2.1.7 on 2019-02-20 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0003_auto_20190220_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress_quantity',
            name='user_id',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
