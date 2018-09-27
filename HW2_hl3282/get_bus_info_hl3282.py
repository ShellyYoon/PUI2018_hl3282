#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:07:39 2018

@author: lihanxing
"""
from __future__ import print_function
import json 
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys 
apikey=sys.argv[1]
busline=sys.argv[2]
csv=sys.argv[3]
if not len(sys.argv) == 4:
    print("invalid number of arguments. Please input 3 arguments like: python get_bus_info_hl3282 <MTA_KEY> <BUS_LINE> <BUS_LINE.csv>")
    sys.exit()
mtaurl="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey,busline)

response = urllib.urlopen(mtaurl)
data = response.read().decode("utf-8")
dataDict = json.loads(data)

outputcsvfile=open(csv,"w")
outputcsvfile.write("Latitude,Longitude,Stop Name,Stop Status\n")
buslists = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
for i in range(0,len(buslists)):
    latitude = buslists[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = buslists[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    try:
        stop_name = buslists[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        stop_status = buslists[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    except LookupError:
        stop_name = "N/A"
        stop_status = "N/A"
    outputcsvfile.write("%s,%s,%s,%s\n"%(latitude,longitude,stop_name,stop_status))
outputcsvfile.close()

