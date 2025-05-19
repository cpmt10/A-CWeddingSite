
##
# Flask script to connect to the DB and get guest data.
##
import os
from flask import Flask, render_template, request, Response, redirect, url_for, session

# Create flask object
app = Flask(__name__)

@app.route('/landing_validation', methods=['GET', 'POST'])
def landing_validation():
    if request.method == 'POST':
        password = request.form.get('password')

        ## Placeholder: we need to check if the password is a valid id in the database (exists)
        ## if it's not -> error, stay in landing.html
        ## if it is -> redirect and gather the guest data.
        headGuestId= "placeholderId"
        app.secret_key = headGuestId
        ## Right now just checking if true to keep progam running -> to be fixed.
        if (True):
            return redirect('get_party')

        ## else send error message on landing screen

@app.route('/get_party')
def get_party():
    session.get('headGuestId')
    
    ## Placeholder as well
    partyList = []
    return render_template('index.html', partyList=partyList)