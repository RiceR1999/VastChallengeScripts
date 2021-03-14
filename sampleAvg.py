import csv
import sys
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
#arg 1 is sample location
parser.add_argument('--location', help='yields net sample count for a specific location')
#arg 2 is sample chemical

sheet = open('readings.csv')
csv_sheet = csv.reader(sheet)
next(csv_sheet)
sample_id = [] #0
#Sample value is located in index 1 however for this script its unnecessary to populate
sample_locations = [] #2
string_dates = [] #3
sample_measure = [] #4
datetime_dates = []
sample_counts = [] 

for row in csv_sheet:
    sample_id.append(row[0])
    sample_locations.append(row[2]) 
    string_dates = row[3]
    datetime_dates.append(datetime.strptime(string_dates, '%d-%b-%y'))
    sample_measure.append(row[4])

args = parser.parse_args()
if args.location:
    sampleCountForSensor(location)
else:
    netSampleCount()

def netSampleCount ():
    #enddate = datetime_dates[len(datetime_dates)-1]
    startyear = datetime_dates[0].year
    startweek = datetime_dates[0].isocalendar()[1]
    for date in datetime_dates:
        week = date.isocalendar()[1] + ((date.isocalendar()[0] - startyear) * 52)
        while len(sample_counts) < week:
         sample_counts.append(0)
        sample_counts[week-startweek] += 1
    print (sample_counts)

def sampleCountForSensor(location):
    samplelocation = location
    startyear = datetime_dates[0].year
    startweek = datetime_dates[0].isocalendar()[1]
    x = 0
    for date in datetime_dates:
        currLocation = sample_locations[x]
        week = date.isocalendar()[1] + ((date.isocalendar()[0] - startyear) * 52)
        while len(sample_counts) < week:
            sample_counts.append(0)
        if samplelocation == currLocation:
            sample_counts[week-startweek] += 1
        x += 1
    print (sample_counts)



