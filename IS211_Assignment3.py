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


logging.basicConfig(filename="errors.log", level=logging.ERROR)
logger = logging.getLogger("assignment2_IS211")


# This Takes the content and processes it line by line
def processData(files):
    # Takes the content and processes it line by line#
    data = StringIO(files)
    # reads csv file
    csv_reader = csv.reader(data, delimiter=',')

    next(csv_reader)
    dataList = []  # store's the  data from csv
    for line in csv_reader:
        dataList.append(line)
    return dataList


imageList = []  # store browsers image


def imageHits(dataList):
    count = 0
    imageIteration = 0

    # Searches for all hits that are for an image file #
    for line in dataList:  # iterate the data in the list
        findList = re.findall('([-\w]+\.(?:jpg|gif|png))', line[0])  # extract the extension part using

        if len(findList) > 0:
            imageIteration += 1
            imageList.append()

        count += 1  # increment counter

    imagePercent = (imageIteration / count) * 100  # calculates percentage
    imagePercent = round(imagePercent, 1)
    print("Images will account for {} % of the requests".format(imagePercent))


# part IV
def browserType(imageList):
    browserCounts = {}  # dict

    browserList = []  # hold
    for line in imageList:
        browserType = re.findall("(?i)(firefox|msie|chrome|safari)[/\s]([\d.]+)",
                                 line[2])

        browserList.append(browserType)  # appends the regular expression
    for browsers in browserList:
        if browsers[0][0] not in browserCounts:
            browserCounts[browsers[0][0]] = 1  # if the  browwer is not in dictionary add and make count
        else:
            browserCounts[browsers[0][0]] += 1  # if the browser is in dictionary add the number of times by one

    browserT = list()  # list to hold tuples
    for key, value in list(browserCounts.items()):
        browserT.append((value, key))

    browserT.sort(reverse=True)  # rearrange the  tuples from largest  to smallest

    print("The most popular browser is {} with {} hits".format(browserT[0][1], browserT[0][0]))


# main function that runs when
def main():
    """Main function"""

    global csvData
    commandParser = argparse.ArgumentParser(description="Send a ­­url parameter to the script")

    commandParser.add_argument("--url", type=str, help="Link to the csv file")

    args = commandParser.parse_args()

    if not args.url:
        exit()

    # call downloadData function and store in csvData
    try:
        csvData = downloadData(args.url)
    except:
        # Print message and exit application if error occurs
        print("An error has occured. Please try again")
        exit()
    # takes the csvData and passes  it to processData and saves it
    browserData = processData(csvData)
    imageHits(browserData)
    browserType()


# Call the main function when script runs
if __name__ == "__main__":
    main()
