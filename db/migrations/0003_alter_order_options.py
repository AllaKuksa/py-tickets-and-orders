# Generated by Django 4.0.2 on 2024-01-10 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_user_order_ticket_alter_movie_actors_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at']},
        ),
    ]