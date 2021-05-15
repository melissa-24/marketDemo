# Generated by Django 3.2 on 2021-05-14 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketApp', '0005_auto_20210514_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='catCreatedAt',
        ),
        migrations.RemoveField(
            model_name='category',
            name='catUpdatedAt',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='shopCreatedAt',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='shopUpdatedAt',
        ),
        migrations.AddField(
            model_name='category',
            name='theUser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='marketApp.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='theOwner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ownerProducts', to='marketApp.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='theProducts', to='marketApp.shop'),
        ),
    ]
