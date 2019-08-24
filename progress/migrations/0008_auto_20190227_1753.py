# Generated by Django 2.1.7 on 2019-02-27 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('progress', '0007_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='uploaded_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.CharField(blank=True, default=1, max_length=255),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.ImageField(upload_to='documents/'),
        ),
    ]
