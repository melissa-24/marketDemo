# Generated by Django 3.2 on 2021-05-14 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='acct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='marketApp.acct'),
        ),
    ]
