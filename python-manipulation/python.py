import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime
filename = input("Enter the filename: ");
with open(filename) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

timestamps_list = []
source_list = []
time_list = []
count_list = []
for ad in content:
        #getting each attributes
    timestamps = ad.split(',')[0]
    source = ad.split('%3A')[1].split('&q=')[0]
    time = ad.split(',')[3]
    count = ad.split(',')[4]
    print(timestamps+','+source+','+time+','+count)


