# Generated by Django 4.1 on 2022-10-02 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teleka', '0006_alter_member_id_alter_saccoadmin_id_withdraw_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Desposit',
            new_name='Deposit',
        ),
    ]