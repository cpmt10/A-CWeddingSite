##
# Flask script to connect to the DB and get guest data.
# New page to handle all of flasks routing. Here we can make use as a bridge for database calls
##
from flask import (
    render_template,
    request,
    redirect,
    session,
    Blueprint,
)

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def landing_validation():
    if request.method == "POST":
        password = request.form.get("password")
        print(password)

        ## Placeholder: we need to check if the password is a valid id in the database (exists)
        ## if it's not -> error, stay in landing.html
        ## if it is -> redirect and gather the guest data.
        headGuestId = "placeholderId"
        views.secret_key = headGuestId
        ## Right now just checking if true to keep progam running -> to be fixed.
        if True:
            return redirect("get_party")
    else:
        return render_template("landing.html")

    ## else send error message on landing screen


@views.route("/get_party")
def get_party():
    session.get("headGuestId")

    ## Placeholder as well
    partyList = []
    return render_template("index.html", partyList=partyList)
