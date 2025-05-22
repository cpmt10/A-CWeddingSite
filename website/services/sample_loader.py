import json
from website import db
from website.models.db_tables import HeadParty, Guest, Passcode


## TEMP METHOD
## Method to load sample data. When real data is ready this method will be deleted
def load_sample_data(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for party_data in data['head_parties']:
        head_party = HeadParty(
            id_pk=party_data['id_pk'],
            first_name=party_data['first_name'],
            initial=party_data['initial'],
            paternal_last_name=party_data['paternal_last_name'],
            maternal_last_name=party_data['maternal_last_name'],
            is_confirmed=party_data['is_confirmed']
        )
        db.session.add(head_party)
        db.session.flush()

        if 'passcode' in party_data:
            passcode = Passcode(
                id_pk=party_data['passcode']['id_pk'],
                head_party_fk=head_party.id_pk
            )
            db.session.add(passcode)

        for guest_data in party_data.get('guests', []):
            guest = Guest(
                id_pk=guest_data['id_pk'],
                first_name=guest_data['first_name'],
                initial=guest_data['initial'],
                paternal_last_name=guest_data['paternal_last_name'],
                maternal_last_name=guest_data['maternal_last_name'],
                head_party_fk=head_party.id_pk
            )
            db.session.add(guest)

    db.session.commit()
