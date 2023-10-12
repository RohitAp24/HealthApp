# Generated by Django 4.2.1 on 2023-06-05 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('status', models.CharField(choices=[('booked', 'Booked'), ('cancelled', 'Cancelled')], max_length=20)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.customer')),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.appointment')),
            ],
            options={
                'unique_together': {('Doctor', 'appointment_date', 'appointment_time')},
            },
        ),
    ]