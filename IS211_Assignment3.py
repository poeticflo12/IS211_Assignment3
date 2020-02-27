# url="http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv"
import logging
import urllib.request
from io import StringIO
import csv
import re
import argparse
import datetime


# This reads and downloads the data from url that was given
def downloadData(url):
    # downloads contents
    info = urllib.request.urlopen(url).read().decode
    return info


# logging.basicConfig(filename="errors.log", level=logging.ERROR)
# logger = logging.getLogger("assignment2_IS211")


# Processes datafile in CSV format
# Takes the content and processes it line by line
def processData(files):
    # Takes the content and process line by line#
    data = StringIO(files)
    # read csv file
    csv_reader = csv.reader(data, delimiter=',')
    # the below statement will skip the first row
    next(csv_reader)
    dataList = []  # store data from csv
    for line in csv_reader:
        # store's data
        dataList.append(line)
    return dataList  # return the list containing values from csv


imageList = []  # store browsers with image extension
