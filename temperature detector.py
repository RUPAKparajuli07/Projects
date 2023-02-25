import tkinter as tk
import requests

# Enter your OpenWeatherMap API key here
API_KEY = 'bc295a4bc8727b69c6df749ba9cc88be'

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    weather_data = response.json()
    temp = round(weather_data['main']['temp'] - 273.15, 2)
    feels_like = round(weather_data['main']['feels_like'] - 273.15, 2)
    weather = weather_data['weather'][0]['description']
    return (temp, feels_like, weather)

def update_weather():
    city = city_entry.get()
    if city:
        try:
            temp, feels_like, weather = get_weather(city)
            temp_label.config(text=f'Temperature: {temp}°C', fg='white', bg='#434343')
            feels_like_label.config(text=f'Feels Like: {feels_like}°C', fg='white', bg='#434343')
            weather_label.config(text=f'Weather: {weather}', fg='white', bg='#434343')
        except:
            temp_label.config(text='Could not fetch weather data.', fg='white', bg='#434343')
            feels_like_label.config(text='', bg='#434343')
            weather_label.config(text='', bg='#434343')
    else:
        temp_label.config(text='Please enter a city name.', fg='white', bg='#434343')
        feels_like_label.config(text='', bg='#434343')
        weather_label.config(text='', bg='#434343')

# Create the main window
root = tk.Tk()
root.geometry('400x200')
root.configure(bg='#434343')
root.title('Weather App')

# Create the input section
input_frame = tk.Frame(root, bg='#434343')
input_frame.pack(pady=10)
city_entry = tk.Entry(input_frame, width=20, font=('Calibri', 16))
city_entry.pack(side=tk.LEFT, padx=5)
submit_button = tk.Button(input_frame, text='Submit', font=('Calibri', 14), command=update_weather)
submit_button.pack(side=tk.LEFT)

# Create the output section
output_frame = tk.Frame(root, bg='#434343')
output_frame.pack()
temp_label = tk.Label(output_frame, font=('Calibri', 20), bg='#434343')
temp_label.pack(pady=5)
feels_like_label = tk.Label(output_frame, font=('Calibri', 16), bg='#434343')
feels_like_label.pack(pady=5)
weather_label = tk.Label(output_frame, font=('Calibri', 16), bg='#434343')
weather_label.pack(pady=5)

root.mainloop()
