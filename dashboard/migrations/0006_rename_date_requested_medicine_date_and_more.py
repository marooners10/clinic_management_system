# Generated by Django 5.1.1 on 2025-01-31 03:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_rename_date_medicine_date_requested_medicine_status_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='date_requested',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='status',
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_category',
            field=models.CharField(choices=[('Oral', 'Oral'), ('Topical', 'Topical'), ('Injectable', 'Injectable'), ('Inhalable', 'Inhalable'), ('Transdermal', 'Transdermal')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_quantity',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.patient'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
