# Generated by Django 4.2.16 on 2024-10-20 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0002_alter_quiz_options_alter_quiz_difficulty'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='score',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='result',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizApp.quiz'),
        ),
    ]
