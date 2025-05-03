import os

temp = os.system("vcgencmd measure_temp")
uptime = os.system("uptime")

print(f"This pi has been running for: {uptime} and the temperature is: {temp}.")