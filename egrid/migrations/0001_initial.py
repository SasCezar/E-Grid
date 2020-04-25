# Generated by Django 3.0.3 on 2020-04-25 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=5, max_digits=9, null=True)),
                ('long', models.DecimalField(decimal_places=5, max_digits=9, null=True)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Address',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1024)),
                ('specification', models.TextField()),
                ('image_url', models.CharField(max_length=512, null=True)),
                ('file_url', models.CharField(max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('org_type', models.CharField(max_length=30)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egrid.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egrid.Organization')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egrid.Product')),
            ],
        ),
        migrations.CreateModel(
            name='GatheringCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('supervisor', models.CharField(max_length=30)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egrid.Address')),
                ('administrated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egrid.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='FinishedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('donation', models.BinaryField(default=False)),
                ('producer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egrid.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Dispatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finished_product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egrid.FinishedProduct')),
                ('gathering_center_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egrid.GatheringCenter')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egrid.Order')),
            ],
            options={
                'unique_together': {('order_id', 'finished_product_id', 'gathering_center_id')},
            },
        ),
    ]
