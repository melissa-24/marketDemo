# Generated by Django 3.2.1 on 2021-05-17 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=45)),
                ('lastName', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('userCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('userUpdatedAt', models.DateTimeField(auto_now=True)),
                ('acct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='marketApp.acct')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopName', models.CharField(max_length=45)),
                ('shopDescription', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='marketApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=45)),
                ('itemDescription', models.TextField()),
                ('itemPrice', models.CharField(max_length=45)),
                ('itemImg', models.CharField(max_length=255)),
                ('itemCount', models.CharField(max_length=45)),
                ('categories', models.ManyToManyField(related_name='products', to='marketApp.Category')),
                ('shop', models.ManyToManyField(related_name='theProducts', to='marketApp.Shop')),
                ('theOwner', models.ManyToManyField(related_name='ownerProducts', to='marketApp.User')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='theUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='marketApp.user'),
        ),
    ]
