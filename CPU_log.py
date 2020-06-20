#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 01:15:21 2020

@author: Hans
"""

# This program log Mac GPS, RAM, network usage 
# Combine with TG pro log file, can detect potential issue

import psutil
import time
from datetime import datetime
import pandas as pd

# Sleep for four minutes first, coz the screen sleep take place in five minutes
time.sleep(240)

#  Sleep the program until start of a minute
dt0 = datetime.today()
second = dt0.strftime("%S")
while second != "00":
    time.sleep(0.1)
    dt0 = datetime.today()
    second = dt0.strftime("%S")
else:
    datetime0 = dt0.strftime("%Y-%m-%d %H:%M:%S")
    print("start at %s" % datetime0)

# Main log program 
df = pd.DataFrame()
for i in range(3):
    dt = datetime.today()
    date1 = dt.strftime("%Y-%m-%d")
    time1 = dt.strftime("%H:%M:%S")
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    network_all = psutil.net_io_counters(pernic=True)
    en0 = network["en0"]
    df1 = pd.DataFrame(
        {"Date":[date1],
         "Time":[time1],
         "CPU":[cpu],
         "RAM":[ram],
         "Byte_sent":[en0[0]],
         "Byte_received": [en0[1]]})
    df = df.append(df1)
    time.sleep(2)

df.to_excel("CPU_log " + str(datetime0) +".xlsx")



