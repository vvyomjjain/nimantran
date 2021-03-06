# Generated by Django 2.0.3 on 2018-03-31 05:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter an event cateory(e.g. Marriage, Birthday etc.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Provide a title to your event.', max_length=200)),
                ('description', models.CharField(help_text='Briefly describe in 500 chars.', max_length=500)),
                ('dateFrom', models.DateField()),
                ('dateTo', models.DateField()),
                ('public', models.BooleanField(default=True)),
                ('cateory', models.ManyToManyField(help_text='Select a cateory for this event', to='catalog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this invite', primary_key=True, serialize=False)),
                ('note', models.CharField(help_text='A personalised note for the guest', max_length=1000, null=True)),
                ('status', models.CharField(choices=[('i', 'Interested'), ('g', 'Going'), ('n', 'Not going')], default='n', help_text='Interest in the event', max_length=1)),
                ('event', models.ForeignKey(help_text='select the event for this event', on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Event')),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(help_text="Person's phone number")),
                ('dob', models.DateField(help_text='Date of Birth', null=True)),
                ('email', models.EmailField(help_text='Email id', max_length=254)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(help_text='address of the venue', max_length=500)),
                ('capacity', models.IntegerField(help_text='Maximum capacity of the venue')),
            ],
        ),
        migrations.AddField(
            model_name='invitation',
            name='invitee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.People'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.People'),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(help_text='Select the venue', on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Venue'),
        ),
    ]
