# Generated by Django 3.0 on 2022-10-19 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teleka', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='member_id',
            new_name='member_id_att',
        ),
    ]