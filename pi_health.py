import os

#temp = os.system("vcgencmd measure_temp")
#uptime = os.system("uptime")

print(f"This pi has been running for: {os.system("uptime")} and the temperature is: {os.system("vcgencmd measure_temp")}.")
