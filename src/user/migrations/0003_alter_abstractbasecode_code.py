# Generated by Django 4.0.4 on 2022-06-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_abstractbasecode_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractbasecode',
            name='code',
            field=models.CharField(max_length=150),
        ),
    ]
