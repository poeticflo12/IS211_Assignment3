# url="http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv"
import logging
from io import StringIO
import urllib.request
import argparse
import datetime
import csv
import re



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
    # reads csv file
    csv_reader = csv.reader(data, delimiter=',')
    # the below statement will skip the first row
    next(csv_reader)
    dataList = []  # store's the  data from csv
    for line in csv_reader:
        # store's data
        dataList.append(line)
    return dataList


imageList = []  # store browsers with image extension


def imageHits(dataList):
    count = 0
    imageIteration = 0

    # Searches for all hits that are for an image file #
    for line in dataList:  # iterate the data in the list
        findList = re.findall('([-\w]+\.(?:jpg|gif|png))', line[0])  # extract the extension part using
        # regular expression

        if len(findList) > 0:
            imageIteration += 1
            imageList.append()

        count += 1  # increment counter for entry to move to the next line

    imagePercent = (imageIteration / count) * 100  # calculate percentage of images extensions
    imagePercent = round(imagePercent, 1)  # round off to one decimal place
    print("Requested images account for {} % of the requests".format(imagePercent))  # print the percentage
