# Generated by Django 3.1.7 on 2021-04-13 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_comment_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_moderated',
            field=models.BooleanField(default=False),
        ),
    ]
