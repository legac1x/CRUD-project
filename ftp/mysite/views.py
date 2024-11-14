from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import ScheduleForm
from .models import Schedule

def index(request):
    form = ScheduleForm()
    schedules = Schedule.objects.all()
    return render(request, 'index.html', {'form': form, 'schedules': schedules})

def create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/')

def edit(request, id):
    try:
        sch = Schedule.objects.get(id=id)
        if request.method == 'POST':
            form = ScheduleForm(request.POST, instance=sch)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/')
        else:
            form = ScheduleForm(instance=sch)
            return render(request, 'edit.html', {'form': form})
    except:
        return HttpResponseNotFound('<h2>Предмета в расписании нет!</h2>')

def delete(request, id):
    try:
        sch = Schedule.objects.get(id=id)
        sch.delete()
        return HttpResponseRedirect('/')
    except:
        return HttpResponseNotFound('<h2>Предмета в расписании нет!</h2>')