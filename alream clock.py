import datetime
import pytz
from playsound import playsound
tz = pytz.timezone('Asia/Kathmandu')
now = datetime.datetime.now(tz)
offset = now.strftime('%z')

alarm_time = input("Enter the time of alarm to be set (HH:MM:SS):\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()

print("Setting up alarm...")
print("GMT offset:", offset)

while True:
    now = datetime.datetime.now(tz)
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    current_time = now.strftime("%I:%M:%S %p")
    print("Current time:", current_time)
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    playsound('audio.mp3')
                    break
                    
