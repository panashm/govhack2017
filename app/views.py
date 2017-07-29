from __future__ import print_function # In python 2.7
from flask import render_template, flash, redirect, session, url_for, request, g
from urlparse import urlparse, urljoin
import smtplib
import sys
from datetime import date, datetime, time, timedelta
import time
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from app import app, db, lm, admin, BaseView, expose, ModelView, bcrypt
#from .forms import searchForm, newEntryForm, item_choices, day_choices, search_choices, loginForm
from .models import User

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


#route for the main page    
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('index.html')


@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('about.html')

    
    
if __name__ == "__main__":
    app.run()
 