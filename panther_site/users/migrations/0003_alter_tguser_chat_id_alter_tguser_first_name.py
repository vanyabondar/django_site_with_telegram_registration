# Generated by Django 4.0.6 on 2022-07-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_tguser_chat_id_alter_tguser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tguser',
            name='chat_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
