# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class ServiceDevelopmentCallsession(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    caller_id = models.CharField(max_length=100, blank=True, null=True)
    field_language = models.ForeignKey('ServiceDevelopmentLanguage', models.DO_NOTHING, db_column='_language_id', blank=True, null=True)  # Field renamed because it started with '_'.
    service = models.ForeignKey('ServiceDevelopmentVoiceservice', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ServiceDevelopmentKasadakauser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_development_callsession'

class ServiceDevelopmentCallsessionstep(models.Model):
    time = models.DateTimeField()
    description = models.CharField(max_length=1000, blank=True, null=True)
    session = models.ForeignKey(ServiceDevelopmentCallsession, models.DO_NOTHING)
    field_visited_element = models.ForeignKey('ServiceDevelopmentVoiceserviceelement', models.DO_NOTHING, db_column='_visited_element_id', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'service_development_callsessionstep'


class ServiceDevelopmentChoice(models.Model):
    voiceserviceelement_ptr = models.ForeignKey('ServiceDevelopmentVoiceserviceelement', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'service_development_choice'


class ServiceDevelopmentChoiceoption(models.Model):
    voiceservicesubelement_ptr = models.ForeignKey('ServiceDevelopmentVoiceservicesubelement', models.DO_NOTHING, primary_key=True)
    field_redirect = models.ForeignKey('ServiceDevelopmentVoiceserviceelement', models.DO_NOTHING, db_column='_redirect_id', blank=True, null=True)  # Field renamed because it started with '_'.
    parent = models.ForeignKey(ServiceDevelopmentChoice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'service_development_choiceoption'


class ServiceDevelopmentKasadakauser(models.Model):
    caller_id = models.CharField(unique=True, max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    creation_date = models.DateTimeField()
    modification_date = models.DateTimeField()
    language = models.ForeignKey('ServiceDevelopmentLanguage', models.DO_NOTHING, blank=True, null=True)
    service = models.ForeignKey('ServiceDevelopmentVoiceservice', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'service_development_kasadakauser'


class ServiceDevelopmentLanguage(models.Model):
    name = models.CharField(unique=True, max_length=100)
    code = models.CharField(unique=True, max_length=10)
    eight = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)
    error_message = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)
    five = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)
    four = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)
    nine = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)
    one = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)
    post_choice_option = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)
    pre_choice_option = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)
    select_language = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)
    seven = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)
    six = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)
    three = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)
    two = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)
    voice_label = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)
    zero = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'service_development_language'


class ServiceDevelopmentMessagepresentation(models.Model):
    voiceserviceelement_ptr = models.ForeignKey('ServiceDevelopmentVoiceserviceelement', models.DO_NOTHING, primary_key=True)
    final_element = models.BooleanField()
    field_redirect = models.ForeignKey('ServiceDevelopmentVoiceserviceelement', models.DO_NOTHING, db_column='_redirect_id', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'service_development_messagepresentation'


class ServiceDevelopmentRecord(models.Model):
    voiceserviceelement_ptr = models.ForeignKey('ServiceDevelopmentVoiceserviceelement', models.DO_NOTHING, primary_key=True)
    repeat_recording_to_caller = models.BooleanField()
    ask_confirmation = models.BooleanField()
    max_time_input = models.IntegerField()
    field_redirect = models.ForeignKey('ServiceDevelopmentVoiceserviceelement', models.DO_NOTHING, db_column='_redirect_id', blank=True, null=True)  # Field renamed because it started with '_'.
    ask_confirmation_voice_label = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING, blank=True, null=True)
    final_voice_label = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING, blank=True, null=True)
    input_category = models.ForeignKey('ServiceDevelopmentUserinputcategory', models.DO_NOTHING, blank=True, null=True)
    not_heard_voice_label = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING, blank=True, null=True)
    repeat_voice_label = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_development_record'


class ServiceDevelopmentSpokenuserinput(models.Model):
    audio = models.CharField(max_length=100)
    time = models.DateTimeField()
    description = models.CharField(max_length=1000, blank=True, null=True)
    category = models.ForeignKey('ServiceDevelopmentUserinputcategory', models.DO_NOTHING)
    session = models.ForeignKey(ServiceDevelopmentCallsession, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'service_development_spokenuserinput'


class ServiceDevelopmentUserinputcategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)
    service = models.ForeignKey('ServiceDevelopmentVoiceservice', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'service_development_userinputcategory'


class ServiceDevelopmentVoicefragment(models.Model):
    audio = models.CharField(max_length=100)
    language = models.ForeignKey(ServiceDevelopmentLanguage, models.DO_NOTHING)
    parent = models.ForeignKey('ServiceDevelopmentVoicelabel', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'service_development_voicefragment'


class ServiceDevelopmentVoicelabel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_development_voicelabel'


class ServiceDevelopmentVoiceservice(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    creation_date = models.DateTimeField()
    modification_date = models.DateTimeField()
    active = models.BooleanField()
    registration = models.CharField(max_length=15)
    registration_language = models.BooleanField()
    registration_name = models.BooleanField()
    field_start_element = models.ForeignKey('ServiceDevelopmentVoiceserviceelement', models.DO_NOTHING, db_column='_start_element_id', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'service_development_voiceservice'


class ServiceDevelopmentVoiceserviceSupportedLanguages(models.Model):
    voiceservice = models.ForeignKey(ServiceDevelopmentVoiceservice, models.DO_NOTHING)
    language = models.ForeignKey(ServiceDevelopmentLanguage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'service_development_voiceservice_supported_languages'
        unique_together = (('voiceservice', 'language'),)


class ServiceDevelopmentVoiceserviceelement(models.Model):
    voiceservicesubelement_ptr = models.ForeignKey('ServiceDevelopmentVoiceservicesubelement', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'service_development_voiceserviceelement'


class ServiceDevelopmentVoiceservicesubelement(models.Model):
    creation_date = models.DateTimeField()
    modification_date = models.DateTimeField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    service = models.ForeignKey(ServiceDevelopmentVoiceservice, models.DO_NOTHING)
    voice_label = models.ForeignKey(ServiceDevelopmentVoicelabel, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_development_voiceservicesubelement'
