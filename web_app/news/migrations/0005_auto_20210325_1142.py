# Generated by Django 3.1.7 on 2021-03-25 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210323_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_words_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
