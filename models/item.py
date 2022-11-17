from db import db
# hei ALisa

class ItemModel(db.Model):
    __tablename__ = "snakes"

    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String)
    latin_name = db.Column(db.String)
    location = db.Column(db.String)
    date = db.Column(db.String)

    def __init__(self, species, latin_name, location, date):
        self.species = species
        self.latin_name = latin_name
        self.location = location
        self.date = date

    def json(self):
        return {
                "ქართული დასახელება" : self.species,
                "ლათინური დასახელება" : self.latin_name,
                "დაფიქსირების ადგილი" : self.location,
                "დაფიქსირების თარიღი" : self.date
                }


    @classmethod
    def find_by_name(cls, species):
        return cls.query.filter_by(species=species).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

