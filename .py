import psutil

battery = psutil.sensors_battery()
percent = float(battery.percent)
print(f'No momento você tem {percent}% de bateria!!')
