# Generated by Django 5.0.1 on 2024-01-18 05:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0010_alter_agent_organisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Leads.userprofile'),
        ),
    ]
