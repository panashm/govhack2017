from __future__ import print_function, division # In python 2.7
from flask import render_template, flash, redirect, session, url_for, request, g
from urlparse import urlparse, urljoin
import smtplib
import sys
from datetime import date, datetime, time, timedelta
import time
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from app import app, lm, admin, BaseView, expose, ModelView, bcrypt
#from .forms import searchForm, newEntryForm, item_choices, day_choices, search_choices, loginForm
import pandas as pd
import numpy as np

subjects=[15210, 15240, 15360, 15120, 15050]

filenames = ["data/2014.csv", "data/2014.csv", "data/2015.csv", "data/2016.csv"] # Fill in remaining files.
df1 = pd.DataFrame()
for filename in filenames:
    df1 = df1.append(pd.read_csv(filename))
    
subjectDict = {}

num = 0
for n in range(len(subjects)):
    print("hello world")
    subjectDict[subjects[num]] = []
    print(subjects[num])
    year = 2014
    for n in range(len(filenames)):
        df1_filtered = df1[(df1['subject'] == subjects[num]) & (df1['year'] == year)]
        #print(df1_filtered)
        totalF = df1_filtered['t_female'].sum()
        print("total female",year, totalF)

        totalM = df1_filtered['t_male'].sum()
        print("total male",year, totalM)

        if totalF or totalM > 0:
            proportion = (totalF/(totalF+totalM))*100
            print("proportion is", proportion, totalF, totalM)
        year += 1
        subjectDict[subjects[num]].append(proportion)
    num +=1
    
print(subjectDict)

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('AdminIndex.html')
        
admin.add_view(MyView(name='Hello'))

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


#function to get subject
#route for the main page    
@app.route("/", methods=['GET', 'POST'])
def main():
    
    
    return render_template('index.html', subjectDict = subjectDict)


@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')

@app.route("/datasets", methods=['GET'])
def dataset():
    return render_template('dataset.html')
    
if __name__ == "__main__":
    app.run()
 