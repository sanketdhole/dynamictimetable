from django.shortcuts import render
from timetable.models import timetable

def index(request):
    rawobjects = timetable.objects.all()
    objects = []
    times = ['8 AM','9 AM','10 AM','11 AM','12 PM','1 PM','2 PM','3 PM','4 PM','5 PM']
    days = ['Mon','Tue','Wed','Thu','Fri','Sat']
    counter = 0
    for day in range(len(days)):
        list = []
        for time in range(len(times)):
            list.append(rawobjects[counter].__dict__)
            counter+=1
        objects.append(list)
    context = {'obj' : objects,'times':times,'days':days,'counter':counter}
    return render(request,'timetable/timetable.html',context)
