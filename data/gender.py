import urllib3, re
import pandas as pd
import numpy as np

#setting up urllib
http = urllib3.PoolManager()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def gender(name):

    #get data from gender prediction API
    genderAPI = "https://api.bundle.io/v1/nametogender?name="+name+"&api_key=KgXjmD0kETqhUmZJv4zMb1ORs"

    response = http.request('GET', genderAPI)

    #get gender field
    array = re.split(':|,|\n',response.data.decode('utf-8'))

    #printing gender
    return array[3].replace("\"", '')

def getListOfNames(df):
    full_names = df['Student name'].tolist()

    first_names = {}
    for full_name in full_names:
        if (len(full_name.split(", ")) > 1):
            first_names[full_name.split(", ")[1].split()[0]] = 1
        else:
            first_names[full_name] = 1
    return list(first_names)


# Loads our stored dictionary with associated genders for names in our dataset.
# Sometimes this function may crash, this is usually caused by either an Unexpected
# special character in the name we're passing that doesn't fit in unicode8 OR
# the API messed up in some way.
# Just restart and resume from where i left off. Alter the listOfName entries left to process.
def load_genders(year):

    df = pd.read_csv(year+".csv")
    listOfNames = getListOfNames(df)
    print(len(listOfNames))

    i = 0
    for name in listOfNames:
        print(str(i)+'\t'+name)
        genders = np.load('all_genders.npy').item()
        if name not in genders:
            genders[name] = gender(name)
            np.save('all_genders.npy', genders)

        i += 1

    print(genders)
