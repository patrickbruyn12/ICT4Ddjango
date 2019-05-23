# Generated by Django 2.0.4 on 2019-05-17 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('seedcode', models.TextField(db_column='seedCode')),
                ('location', models.TextField()),
                ('credit', models.DecimalField(decimal_places=2, max_digits=6)),
                ('availablefrom', models.TextField(db_column='availableFrom')),
                ('availableto', models.TextField(db_column='availableTo')),
                ('status', models.TextField()),
            ],
            options={
                'db_table': 'projects_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectsProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'projects_project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentCallsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('caller_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'service_development_callsession',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentCallsessionstep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'service_development_callsessionstep',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentKasadakauser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caller_id', models.CharField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField()),
                ('modification_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'service_development_kasadakauser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'service_development_language',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentSpokenuserinput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'service_development_spokenuserinput',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentUserinputcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'service_development_userinputcategory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentVoicefragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'service_development_voicefragment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentVoicelabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'service_development_voicelabel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentVoiceservice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('creation_date', models.DateTimeField()),
                ('modification_date', models.DateTimeField()),
                ('active', models.BooleanField()),
                ('registration', models.CharField(max_length=15)),
                ('registration_language', models.BooleanField()),
                ('registration_name', models.BooleanField()),
            ],
            options={
                'db_table': 'service_development_voiceservice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentVoiceservicesubelement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField()),
                ('modification_date', models.DateTimeField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'service_development_voiceservicesubelement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentVoiceserviceSupportedLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'service_development_voiceservice_supported_languages',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentChoiceoption',
            fields=[
                ('voiceservicesubelement_ptr', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='projects.ServiceDevelopmentVoiceservicesubelement')),
            ],
            options={
                'db_table': 'service_development_choiceoption',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentVoiceserviceelement',
            fields=[
                ('voiceservicesubelement_ptr', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='projects.ServiceDevelopmentVoiceservicesubelement')),
            ],
            options={
                'db_table': 'service_development_voiceserviceelement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentChoice',
            fields=[
                ('voiceserviceelement_ptr', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='projects.ServiceDevelopmentVoiceserviceelement')),
            ],
            options={
                'db_table': 'service_development_choice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentMessagepresentation',
            fields=[
                ('voiceserviceelement_ptr', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='projects.ServiceDevelopmentVoiceserviceelement')),
                ('final_element', models.BooleanField()),
            ],
            options={
                'db_table': 'service_development_messagepresentation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevelopmentRecord',
            fields=[
                ('voiceserviceelement_ptr', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='projects.ServiceDevelopmentVoiceserviceelement')),
                ('repeat_recording_to_caller', models.BooleanField()),
                ('ask_confirmation', models.BooleanField()),
                ('max_time_input', models.IntegerField()),
            ],
            options={
                'db_table': 'service_development_record',
                'managed': False,
            },
        ),
    ]