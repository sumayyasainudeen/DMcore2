# Generated by Django 4.1.4 on 2023-08-11 05:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0014_progress_report_status_smo_socialmedia_smo_end_date_and_more'),
    ]

    operations = [
        
       
        
       
        
        migrations.AlterField(
            model_name='daily_leeds_exists',
            name='date',
            field=models.DateField(default=datetime.date(2023, 8, 11)),
        ),
        
       
    ]
