# Generated by Django 3.1.2 on 2020-11-01 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newplo1', '0003_auto_20201031_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_for_admin',
            name='link',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
