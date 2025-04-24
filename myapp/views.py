import requests
from django.shortcuts import render
from myapp.forms import City

def weather_view(request):
    form = City()
    weather_data = {}

    if request.method == 'POST':
        form = City(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_key = 'YOUR_API_KEY'  # Replace with your actual API key
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={"919841353079862d87f8f8385ce640b1"}&units=metric'
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                }

    return render(request, 'weather.html', {'form': form, 'weather': weather_data})

# Create your views here.
