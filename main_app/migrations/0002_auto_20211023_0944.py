# Generated by Django 3.2.8 on 2021-10-23 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=250)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ManyToManyField(to='main_app.Event')),
                ('user', models.ManyToManyField(to='main_app.UserProfile')),
            ],
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
