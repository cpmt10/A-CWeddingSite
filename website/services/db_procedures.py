from website import db
from website.models.db_tables import HeadParty, Guest, Passcode

## This class is meant to function has a repleacement to MySQL's Stored Procedures

## Method to get the information from the entered passcode 
def get_head_party_with_guests_by_passcode(passcode_id):
    # Get the passcode entry first
    passcode = Passcode.query.filter_by(id_pk=passcode_id).first()
    if not passcode:
        return None  

    # Get the head party using the relationship
    head_party = passcode.head_party
    if not head_party:
        return None  # Defensive check, in case of data inconsistency

    # Get the guests linked to this head party
    guests = Guest.query.filter_by(head_party_fk=head_party.id_pk).all()

    return {
        'head_party': head_party,
        'guests': guests
    }

## Method to get the head of party by their ID
def get_head_party_by_id(head_party_id):
    return HeadParty.query.get(head_party_id)

## Method to get the guest by their id 
def get_guests_by_ids(guest_ids):
    return Guest.query.filter(Guest.id_pk.in_(guest_ids)).all()