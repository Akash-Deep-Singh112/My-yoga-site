from django.shortcuts import render
from .models import Destination
def index(request):
    dest1=Destination()
    dest2=Destination()
    dest3=Destination()
    dest1.name='Mumbai'
    dest1.desc='The city that never sleeps'
    dest1.img='destination_1.jpg'
    dest1.price=700
    dest2.name='Delhi'
    dest2.desc='The city that is India capital'
    dest2.img='destination_2.jpg'
    dest2.price=650
    dest3.name='Chennai'
    dest3.desc='The metro city of the south'
    dest3.img='destination_3.jpg'
    dest3.price=600
    dests=[dest1,dest2,dest3]
    return render(request,'index.html',{'dests':dests})
