# Generated by Django 4.1 on 2023-07-19 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0004_lead_file_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='exe_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exe_lead', to='DMcoreapp.user_registration'),
        ),
    ]
