# Generated by Django 3.1.2 on 2020-11-01 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newplo1', '0005_news_for_admin_site_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_for_admin',
            name='site_name',
            field=models.CharField(max_length=30),
        ),
    ]
