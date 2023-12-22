# Generated by Django 4.2.2 on 2023-12-22 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_rename_cashcenters_cashcenter'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeExpenditure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('receipt_number', models.IntegerField()),
                ('description', models.TextField()),
                ('amount_received', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amount_paid', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('update_on', models.DateTimeField(auto_now=True)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.cashcenter')),
                ('paid_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='paid_by', to=settings.AUTH_USER_MODEL)),
                ('paid_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='paid_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
