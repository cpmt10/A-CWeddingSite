from website import db
from website.models.db_tables import HeadParty, Guest, Passcode
import json, os

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

    return {"head_party": head_party, "guests": guests}


## Method to get the head of party by their ID
def get_head_party_by_id(head_party_id):
    return HeadParty.query.get(head_party_id)


## Method to get the guest by their id
def get_guests_by_ids(guest_ids):
    return Guest.query.filter(Guest.id_pk.in_(guest_ids)).all()


def update_party_confirmation(head_party_id, head_confirmed, attending_guest_ids):
    try:
        head = HeadParty.query.get(head_party_id)
        if not head:
            return False, "Encargado no encontrado."

        attending_set = set(int(i) for i in (attending_guest_ids or []))

        # Update head confirmation with the actual form value
        head.is_confirmed = head_confirmed

        # Update guests
        guests = Guest.query.filter_by(head_party_fk=head_party_id).all()
        for g in guests:
            g.is_attending = g.id_pk in attending_set

        db.session.commit()

        update_sample_json()
        return True, None
    except Exception as exc:
        db.session.rollback()
        return False, str(exc)

    except Exception as exc:
        # If database failed to insert data then rollback to before they were inserted to preserve database integrity
        db.session.rollback()
        return False, "Ocurrió un error al guardar la confirmación. Intenta nuevamente."


def update_sample_json():
    try:
        base_dir = os.path.dirname(__file__)
        project_root = os.path.abspath(os.path.join(base_dir, ".."))
        json_file_path = os.path.join(project_root, "data", "sample.json")

        head_parties = HeadParty.query.all()
        data = {"head_parties": [hp.to_dict() for hp in head_parties]}

        if os.path.exists(json_file_path):
            os.remove(json_file_path)

        with open(json_file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        return True, None

    except Exception as e:
        print(f"Error writing backup: {e}")
        return False, str(e)
