# Generated by Django 3.0.8 on 2020-07-04 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rule'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='rule',
            field=models.ForeignKey(db_column='id_rule', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Rule'),
        ),
    ]
