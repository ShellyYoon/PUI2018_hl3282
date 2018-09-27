#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 21:06:54 2018

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
if not len(sys.argv) == 3:
    print("invalid number of arguments. Please input 2 arguments like: python show_bus_locations_hl3282.py <MTA_KEY> <BUS_LINE>")
    sys.exit()
mtaurl="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey,busline)

response = urllib.urlopen(mtaurl)
data = response.read().decode("utf-8")
dataDict = json.loads(data)

buslists = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
print("Bus Line : %s"%(busline))
print("Number of Active Buses : %s"%(len(buslists)))
for i in range(0,len(buslists)):
    latitude=buslists[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude=buslists[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print("Bus %s is at latitude %s and longitude %s"%(i,latitude,longitude))
