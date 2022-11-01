#/user/bin/python3

 

 

 

import sys

 

import datetime

 

dayofweek = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

find=[{},{},{},{},{},{},{}]

with open(sys.argv[1], "rt") as fp:

    rows= fp.readlines()

    for row in rows:

        uber = row.split(",")

        region = uber[0]

        day = uber[1].split("/")

        vehicle = uber[2]

        trip = uber[3]

 

        ofweek = dayofweek[datetime.date(int(day[2]), int(day[0]), int(day[1])).weekday()]

        

        region_day = region + "," + ofweek

        if region in find[ofweek].keys():

            vehicles = int(find[ofweek][region].split(',')[0]) + int(vehicle)

            trips = int(find[ofweek][region].split(',')[1]) + int(trip)

            find[ofweek][region] = str(vehicles) + "," + str(trips)

        else :

            find[ofweek][region] = vehicle + "," + trip

            

print(find)

with open(sys.argv[2],'w') as fp:

    for i in range(7):

        for r in find[i].keys():

            fp.write("%s,%s %s\n" %(r, dayofweek[i], find[i][r]))  
