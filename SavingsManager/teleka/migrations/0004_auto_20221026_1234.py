# Generated by Django 3.0 on 2022-10-26 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teleka', '0003_auto_20221019_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='collateral1_attachements',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='collateral2_attachements',
        ),
        migrations.RemoveField(
            model_name='member',
            name='member_id_att',
        ),
        migrations.RemoveField(
            model_name='member',
            name='member_photo',
        ),
        migrations.RemoveField(
            model_name='member',
            name='next_of_keen_id',
        ),
    ]