# Generated by Django 2.1.1 on 2018-10-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0003_auto_20181029_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='邮箱'),
            preserve_default=False,
        ),
    ]