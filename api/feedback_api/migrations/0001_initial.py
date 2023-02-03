# Generated by Django 4.1.6 on 2023-02-03 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Name')),
            ],
            options={
                'db_table': '"feedback"."service"',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('status', models.CharField(max_length=240, verbose_name='Name')),
                ('assigned_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_api.employee')),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_api.customer')),
                ('service_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feedback_api.service')),
            ],
            options={
                'db_table': '"feedback"."feedback"',
            },
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('Feedback_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feedback_api.feedback')),
                ('employee_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_api.employee')),
            ],
            options={
                'db_table': '"feedback"."action"',
            },
        ),
    ]
