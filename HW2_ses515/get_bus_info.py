from __future__ import print_function

import pylab as pl
import os
import json
import pandas as pd
import sys

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

# %pylab inline
pl.rc('font', size=15)

key = sys.argv(1)
line = sys.argv(2)

if not len(sys.argv) == 3:
    print ("Invalid number of arguments.")
    sys.exit()

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + \
   "a&VehicleMonitoringDetailLevel=calls&LineRef=" + line

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)





next_bus = []
for bus in range(len(busloc)):
    latlong = busloc[bus]['MonitoredVehicleJourney']['VehicleLocation']
    status = busloc[bus]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']['Distances']['PresentableDistance']
    stop = busloc[bus]['MonitoredVehicleJourney']['OnwardCalls']['StopPointName']
    next_bus.append({"latlong": latlong, "status": status, "stop": stop})
   
# why listing same bus multiple times
# for i in range(len(busloc)):
#     print ("{i} is at {location}, {status}, {stop}".format(i=i, location=latlong, status=status, stop=stop))   
