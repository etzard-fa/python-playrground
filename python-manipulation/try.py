import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime
# This makes our works modular and is the beginning of scripting
def count_info(count_sources):
    """this funcntion extracts the attributes for each ads and return the results in dataframe"""

    # create the list of all attributes
    timestamps_list = []
    source_list = []
    time_list = []
    count_list = []

    for ad in count_sources:
        # getting each attributes
        timestamps = ad.split(',')[0]
        source = ad.split('%3A')[1].split('&q=')[0]
        time = ad.split(',')[3]
        count = ad.split(',')[4]

        # appending to a list
        timestamps_list.append(timestamps)
        source_list.append(source)
        time_list.append(time)
        count_list.append(count)


    # putting the results in a dataframe
    df_info = pd.DataFrame({'Timestamps': timestamps_list,
                               'SourceName': source_list,
                               'TimeTaken': time_list,
                               'CountDocument': count_list})
    return df_info


# saving to csv
def save_data(df):
    """this function convert a dataframe into a csv file appending the current date and time"""
    file_time = datetime.datetime.now()
    file_time = file_time.strftime('%Y-%m-%d')
    file_name = 'Release_Post_Count' + file_time + '.csv'

    df.to_csv(file_name, index=False)


# method for scraping
def scrape_data(filename):
    with open(filename) as f:
        content = f.read().splitlines()

    output = "\n".join(" ".join(two_lines) \
                       for two_lines in zip(content[::2], content[1::2])) + (
                 content[-1] if len(content) % 2 != 0 else '')








    # Step 1: Send request to the website to get the page contents


    # extract the data from the ads
    print('Extracting the data')
    scraped_data_df = count_info(count_sources)
    print('Extracting done')
    # save the data to csv format
    save_data(scraped_data_df)
    print('Scraping completed!!\nFile saved')

filename = input("Enter the filename: ");
scrape_data(filename)