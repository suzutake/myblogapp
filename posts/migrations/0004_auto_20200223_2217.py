# Generated by Django 2.2.5 on 2020-02-23 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200223_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumaster',
            name='customer',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='posts.Customer'),
        ),
    ]
