# Generated by Django 2.0.3 on 2019-07-12 16:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget_allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gob', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('Dpa', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('Rpa', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('Total', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cheque_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cheque_no', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('Bank_name', models.CharField(max_length=60)),
                ('Bank_brach', models.CharField(max_length=60)),
                ('Total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChequeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('cheque_image', models.ImageField(upload_to='structures/%Y/%m/%d/')),
                ('issuing_date', models.DateField(default=django.utils.timezone.now)),
                ('uploaded_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Dpp_allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ecode', models.IntegerField(blank=True, null=True)),
                ('Description', models.CharField(max_length=400)),
                ('Gob', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('Dpa', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('Rpa', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('Total', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expenditure_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gob', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('Dpa', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('Rpa', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('Total', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('Financial_year', models.CharField(blank=True, max_length=7, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('Budget_allocation_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pac.Budget_allocation')),
                ('Cheque_details_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pac.Cheque_details')),
            ],
        ),
        migrations.CreateModel(
            name='FinancialYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('finishDate', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='cheque_details',
            name='document_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pac.ChequeImage'),
        ),
        migrations.AddField(
            model_name='budget_allocation',
            name='Dpp_allocation_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pac.Dpp_allocation'),
        ),
        migrations.AddField(
            model_name='budget_allocation',
            name='Financial_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pac.FinancialYear'),
        ),
    ]
