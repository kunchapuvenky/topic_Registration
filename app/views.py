from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def Registration(request):
    d={'tfo':TopicForm(),'wfo':WebpageForm(),'afo':AccessRecordForm()}

    if request.method=='POST':
        tfd=TopicForm(request.POST)
        wfd=WebpageForm(request.POST)
        afd=AccessRecordForm(request.POST)

        if tfd.is_valid() and wfd.is_valid() and afd.is_valid():
            
            NSTFO=tfd.save(commit=False)
            NSTFO.save()

            NSWFO=wfd.save(commit=False)
            NSWFO.topic_name=NSTFO
            NSWFO.save()

            NSAFO=afd.save(commit=False)
            NSAFO.name=NSWFO
            NSAFO.save()

            return HttpResponse('Registration is successful')

        else:
            return HttpResponse('Data is not valid')

    return render(request,'Registration.html',d)