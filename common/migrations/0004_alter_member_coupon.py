# Generated by Django 4.2.2 on 2023-06-30 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_alter_member_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='coupon',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
