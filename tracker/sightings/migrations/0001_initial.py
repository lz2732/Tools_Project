# Generated by Django 2.2.7 on 2019-12-05 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X', models.FloatField(blank=True, help_text='Using decimal degrees for Longitude.')),
                ('Y', models.FloatField(blank=True, help_text='Using decimal degrees for Latitude.')),
                ('Unique_Squirrel_ID', models.CharField(help_text='This is a required field.', max_length=20)),
                ('Hectare', models.CharField(blank=True, max_length=3)),
                ('Shift', models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], help_text='The shift of the sightinghappened.', max_length=2)),
                ('Date', models.DateField(blank=True, help_text='Date of the sighting happened')),
                ('Hectare_Squirrel_Number', models.IntegerField(blank=True, null=True)),
                ('Age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenlie'), ('?', '?')], help_text='The age of the squirrel.', max_length=20)),
                ('Primary_Fur_Color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], help_text='Primary fur color of the squirrel', max_length=20)),
                ('Highlight_Fur_Color', models.CharField(blank=True, max_length=50)),
                ('Combination', models.CharField(blank=True, max_length=70)),
                ('Color_Notes', models.CharField(blank=True, max_length=500)),
                ('Location', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], max_length=20)),
                ('Above_Ground_Sighter_Measurement', models.IntegerField(blank=True, null=True)),
                ('Specific_Location', models.CharField(blank=True, max_length=500)),
                ('Running', models.BooleanField(default=False)),
                ('Chasing', models.BooleanField(default=False)),
                ('Climbing', models.BooleanField(default=False)),
                ('Eating', models.BooleanField(default=False)),
                ('Foraging', models.BooleanField(default=False)),
                ('Other_Activities', models.CharField(blank=True, max_length=500)),
                ('Kuks', models.BooleanField(default=False)),
                ('Quaas', models.BooleanField(default=False)),
                ('Moans', models.BooleanField(default=False)),
                ('Tail_Flags', models.BooleanField(default=False)),
                ('Tail_Twitches', models.BooleanField(default=False)),
                ('Approaches', models.BooleanField(default=False)),
                ('Indifferent', models.BooleanField(default=False)),
                ('Runs_From', models.BooleanField(default=False)),
                ('Other_Interactions', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
