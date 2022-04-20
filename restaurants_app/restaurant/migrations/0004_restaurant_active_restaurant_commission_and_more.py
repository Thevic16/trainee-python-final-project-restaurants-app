# Generated by Django 4.0.4 on 2022-04-19 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_paytype'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='commission',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='max_admins',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='max_branches',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='pay_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='restaurant.paytype'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='food_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='restaurant.foodtype'),
        ),
    ]
