# Generated by Django 4.2 on 2023-04-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_body_post_create_at_post_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
