from django.shortcuts import render
import requests
from django.http import Http404

# Create your views here.

def index(request):
    city = request.GET.get('enteredCity')

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=your_api_key'.format(city)

    try:
        city_weather = requests.get(url.format(city)).json() 
        #request the API data and convert the JSON to Python data   types

        weather = {
            'city':city_weather['name'],    
            'temperature': int((city_weather['main']['temp'] - 32) * 5.0/9.0),
            'description':city_weather['weather'][0]    ['description'],
            'icon':city_weather['weather'][0]['icon'],

        }

    except Exception as e:
        raise Http404('not found')
    
    except KeyError:
        raise Http404('Not found')

    context = {
        'weather':weather
    }

    return render(request, 'weather/index.html' , context) #returns the index.html template
 
