"""
program: get system time and save to file
date: 2024-11-14
"""

import time


def system_info():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    weekday = time.strftime("%A", time.localtime())
    days_in_month = time.strftime("%d", time.localtime())
    return current_time, weekday, f"There are {days_in_month} days in this month."


time_info = system_info()
with open("time_info.txt", "w") as file:
    file.write("\n".join(time_info))

with open("time_info.txt", "r") as file:
    print(file.read())
