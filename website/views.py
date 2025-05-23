##
# Flask script to connect to the DB and get guest data.
# New page to handle all of flasks routing. Here we can make use as a bridge for database calls
##
from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from website.services.db_procedures import (
    get_head_party_with_guests_by_passcode,
    get_head_party_by_id,
    get_guests_by_ids,
)


views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def landing_validation():
    #Checks if the request is a POST
    if request.method == "POST":

        #Gets the password
        password = request.form.get("password")

        #Submits the password for validation
        result = get_head_party_with_guests_by_passcode(password)

        #If results come back with a valid value then proceed
        if result:
            # If data was found then store it in the session for use in the next page
            session["party_data"] = {
                "head_party": result["head_party"].id_pk,
                "guests": [guest.id_pk for guest in result["guests"]],
            }
            # Redirects to the get_party page
            return redirect(url_for("views.get_party"))  
        else:
            # If the code was incorrect then show a pop up and refresh back to landing page
            flash("Codigo invalido. Intenta de nuevo.")
            return render_template("landing.html")

    return render_template("landing.html")


@views.route("/get_party")
def get_party():
    # Loads the party information from the session 
    party_data = session.get("party_data")

    if not party_data:
        # Show pop up of error if the session informtion didnt load correctly
        flash("No se encontró información del grupo. Intenta de nuevo.")
        return redirect(url_for("views.landing_validation"))

    # Gets the ids stored in the sessions and uses them to get the guests information
    head_party = get_head_party_by_id(party_data["head_party"])
    guests = get_guests_by_ids(party_data["guests"])

    # TEMP METHOD
    # Didnt know where to place this method yet but it is meant to join the names correctly
    def format_name(person):
        return f"{person.first_name} {person.initial + '.' if person.initial else ''} {person.paternal_last_name} {person.maternal_last_name or ''}".strip()

    ## stores the head of party name and their guests inside of party_list to see if they load on the website
    party_list = [format_name(head_party)] + [format_name(guest) for guest in guests]

    return render_template("index.html", partyList=party_list, headOfParty=head_party.first_name)

@views.route("/confirm_form")
def confirm_form():
    party_list = request.args.get('party_list')
    return render_template("confirmation_form.html", partyList=party_list)