from django.shortcuts import render
from projects.models import ServiceDevelopmentCallsession

def voiceLabel(request):
    #firstOverview = ServiceDevelopmentCallsession.objects.values("id", "start", "caller_id").order_by("-id")
    firstOverview = ServiceDevelopmentCallsession.objects.all().order_by("-id")
    context = {
        'firstOverview': firstOverview
    }
    return render(request, 'project_index.html', context)

def project_extra(request, pk=None):
    dataRecords = ServiceDevelopmentCallsession.objects.all().order_by("-id")
    context = {
        'dataReecords': dataRecords
    }
    return render(request, 'project_extra.html', context)
