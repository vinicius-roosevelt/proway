# Generated by Django 3.1.1 on 2020-09-30 00:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20200927_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='break_max_record_amount',
        ),
        migrations.RemoveField(
            model_name='games',
            name='break_min_record_amount',
        ),
        migrations.RemoveField(
            model_name='games',
            name='is_max_break_record',
        ),
        migrations.RemoveField(
            model_name='games',
            name='is_min_break_record',
        ),
        migrations.RemoveField(
            model_name='games',
            name='max_season',
        ),
        migrations.RemoveField(
            model_name='games',
            name='min_season',
        ),
        migrations.AddField(
            model_name='games',
            name='game_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data do jogo'),
        ),
    ]