from django.shortcuts import render,HttpResponse
from .models import Team
from cars.models import Car
# Create your views here.
def home(request):
    # return HttpResponse("loremIpsm")
    team_ret=Team.objects.all() #decleraing for calling function from our database
    featured_car=Car.objects.order_by('-created_date').filter(is_featured=True)
    all_car=Car.objects.order_by('-created_date')
    model_fields=Car.objects.values_list('model',flat=True).distinct() #this will give individual data from the database no repeating adn return the value in list
    location_fields=Car.objects.values_list('city',flat=True).distinct()
    build_year=Car.objects.values_list('year',flat=True).distinct()
    body_fields=Car.objects.values_list('body_style',flat=True).distinct()
    transmission=Car.objects.values_list('transmission',flat=True).distinct()

    
    
    data={
        'team':team_ret,
        'ft_car':featured_car,
        'All_car':all_car,
        'model_fields':model_fields,
        'location_fields':location_fields,
        'build_fields':  build_year,
        'body_fields': body_fields,
        'transmission':transmission
    }
    return render(request,'pages/home.html',data)
def about(request):
    team_retn=Team.objects.all()
    data={
        'team':team_retn,
    }
    return render(request,'pages/about.html',data)
def services(request):
    return render(request,'pages/services.html')
def contact(request):
    return render(request,'pages/contact.html')