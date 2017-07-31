import os.path
import re, urllib3
import pandas as pd
import numpy as np
import sys

# READ ME!!!!!
# This file is a mess. Not going to lie.
# You may have to play around with the EXACT titles of each column in the table
# that was scraped from BOSTE website, since they changed things like capitilization
# and format from year to year.
#
# 1. (2+ minutes) run [results_scrape.py] scrapeYear(year) which will output a new csv file.
# 2. (10+ minutes) run [gender.py] load_genders(year) which will update our dictionary of known
#    associative genders.
# 3. (30 seconds) run [results_scrape.py] add_gender(df, year) which will attach the gender field to
#    each entry.
# 4. (10 minutes) run [results_scrape.py] collapse_data(df) which will collapse and minimize our data set size.


# Appends the table found at the url to the (non-)existing csv_file
def append_table(csv_file, url):

    raw_df = pd.read_html(url)[0]

    new_df = pd.DataFrame(columns=['year', 'Student name', 'School name', 'course'])
    for index, row in raw_df.iterrows():
        subjects = re.split("(?<!^)\s+(?=[0-9]{5})(?!.\s)", row["Top band Courses"])
        for subject in subjects:
            df2 = pd.DataFrame([[2016, row['Student Name'], row['School Name'], subject]], columns=['year', 'Student name', 'School name', 'course'])
            new_df = new_df.append(df2)

    # Append to existing
    if os.path.exists(csv_file):
        existing_df = pd.read_csv(csv_file)
        new_df = existing_df.append(new_df)
    new_df = new_df.reset_index(drop=True)

    new_df.to_csv(csv_file, index=False)

# Appends the table found at the url to the (non-)existing csv_file
def append_table(year, url):

    raw_df = pd.read_html(url)[0]

    new_df = pd.DataFrame(columns=['year', 'Student name', 'School name', 'course'])
    for index, row in raw_df.iterrows():
        subjects = re.split("(?<!^)\s+(?=[0-9]{5})(?!.\s)", row["Top Band Courses"])
        for subject in subjects:
            df2 = pd.DataFrame([[year, row['Student Name'], row['School Name'], subject]], columns=['year', 'Student name', 'School name', 'course'])
            new_df = new_df.append(df2)

    # Append to existing
    if os.path.exists(year+".csv"):
        existing_df = pd.read_csv(year+".csv"
        new_df = existing_df.append(new_df)
    new_df = new_df.reset_index(drop=True)

    new_df.to_csv(year+".csv", index=False)

def scrapeYear(year):
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ."):
        i = 1
        while True:
            try:
                url = "http://www.boardofstudies.nsw.edu.au/ebos/static/DSACH_"+year+"_12_"+letter+str(i)+".html"
                print("Scraping..\t", url)
                append_table_2013(year+".csv", url)
                i += 1
            except:
                print ("Unexpected error:", sys.exc_info()[0])
                break

#setting up urllib
def gender(name):

    http = urllib3.PoolManager()

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    #get data from gender prediction API
    genderAPI = "https://api.bundle.io/v1/nametogender?name="+name+"&api_key=KgXjmD0kETqhUmZJv4zMb1ORs"

    response = http.request('GET', genderAPI)

    #get gender field
    array = re.split(':|,|\n',response.data)

    #printing gender
    print(array[3])

def getFirstName(full_name):
    if (len(full_name.split(", ")) > 1):
        return full_name.split(", ")[1].split()[0]
    else:
        return full_name


# Adds associated gender to each row.
# Removes students we could not identify gender for.
def add_gender(df, year):
    genders = np.load('all_genders.npy').item()
    new_df = pd.DataFrame(columns=['year', 'Student name', 'School name', 'course', 'gender'])

    for index, row in df.iterrows():
        if getFirstName(row['Student name']) in genders:
            if genders[getFirstName(row['Student name'])] != 'false':
                df2 = pd.DataFrame([[year, row['Student name'], row['School name'], row['course'], genders[getFirstName(row['Student name'])]]], columns=['year', 'Student name', 'School name', 'course', 'gender'])
                new_df = new_df.append(df2)

    return new_df


# Collapses the data set into rows dependant on school and associated subject result
def collapse_data(df):
    schools = list(set(df['School name'].tolist()))
    subjects = list(set(df['course'].tolist()))

    new_df = pd.DataFrame(columns=['year', 'school', 'subject', 't_band6', 't_male', 't_female'])

    i = 1
    for school in schools:
        print("working on school n"+str(i))
        for subject in subjects:
            male_count = df[(df['School name'] == school) & (df['course'] == subject) & (df['gender'] == 'male')].year.count()
            female_count = df[(df['School name'] == school) & (df['course'] == subject) & (df['gender'] == 'female')].year.count()

            if (male_count != 0 or female_count != 0):
                df2 = pd.DataFrame([[2013, school, subject, male_count + female_count, male_count, female_count]], columns=['year', 'school', 'subject', 't_band6', 't_male', 't_female'])
                new_df = new_df.append(df2)

        i += 1
    new_df = new_df.reset_index(drop=True)
    return new_df
