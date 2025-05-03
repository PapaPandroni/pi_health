import os
import subprocess

temp = subprocess.check_output("vcgencmd measure_temp", shell=True).decode().strip()
uptime = subprocess.check_output("uptime", shell =True).decode().strip()

print(f"This pi has been running for: {uptime} and the temperature is: {temp}.")
