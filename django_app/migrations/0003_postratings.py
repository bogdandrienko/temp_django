# Generated by Django 4.2.2 on 2023-06-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_postcomments'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Рейтинг к публикации',
                'verbose_name_plural': 'Рейтинги к публикациям',
                'ordering': ('-rating', 'post_id'),
            },
        ),
    ]
