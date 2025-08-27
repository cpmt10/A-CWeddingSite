from website import db

# Models to deserialize data from the database directly into a Python Objects in SQLALchemy Format
# These classes are fully customizable and are just placeholders
from website import db


class HeadParty(db.Model):
    __tablename__ = "head_party"

    id_pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    initial = db.Column(db.String(1), nullable=True)
    paternal_last_name = db.Column(db.String, nullable=False)
    maternal_last_name = db.Column(db.String, nullable=True)
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)

    guests = db.relationship(
        "Guest",
        backref="head_party",
        lazy=True,
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    passcode = db.relationship(
        "Passcode",
        backref="head_party",
        uselist=False,
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def to_dict(self):
        return {
            "id_pk": self.id_pk,
            "first_name": self.first_name,
            "initial": self.initial,
            "paternal_last_name": self.paternal_last_name,
            "maternal_last_name": self.maternal_last_name,
            "is_confirmed": self.is_confirmed,
            "passcode": self.passcode.to_dict() if self.passcode else None,
            "guests": [g.to_dict() for g in self.guests],
        }


class Guest(db.Model):
    __tablename__ = "guests"

    id_pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    initial = db.Column(db.String(1), nullable=True)
    paternal_last_name = db.Column(db.String, nullable=False)
    maternal_last_name = db.Column(db.String, nullable=True)
    head_party_fk = db.Column(
        db.Integer,
        db.ForeignKey("head_party.id_pk", ondelete="CASCADE"),
        nullable=False,
    )
    is_attending = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
            "id_pk": self.id_pk,
            "first_name": self.first_name,
            "initial": self.initial,
            "paternal_last_name": self.paternal_last_name,
            "maternal_last_name": self.maternal_last_name,
            "is_attending": self.is_attending,
        }


class Passcode(db.Model):
    __tablename__ = "passcode"

    id_pk = db.Column(db.String, primary_key=True)
    head_party_fk = db.Column(
        db.Integer,
        db.ForeignKey("head_party.id_pk", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    def to_dict(self):
        return {"id_pk": self.id_pk}
