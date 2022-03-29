from django.shortcuts import render

# Create your views here.
import urllib.request
import json


def index(request):
    if request.method == 'POST':

        city = request.POST['city']
        start_url='https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=fd5c9baa6dce93805a53f3d88fed144e'
        url= start_url.replace(" ", "%20")
        source=urllib.request.urlopen(url).read()
        # source = urllib.request.urlopen(
        #     'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=fd5c9baa6dce93805a53f3d88fed144e').read()
        list_of_data = json.loads(source)
        data = {
            "condition": str(city),
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
                          + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + ' C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "main": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": str(list_of_data['weather'][0]['icon']),
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)
