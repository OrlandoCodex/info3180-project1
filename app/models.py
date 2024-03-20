from . import db
# from werkzeug.security import generate_password_hash

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    numBedrms = db.Column(db.Integer)
    numBathrms = db.Column(db.Integer)
    location = db.Column(db.String(80))
    price = db.Column(db.Float)
    propType = db.Column(db.String(10))
    description = db.Column(db.String(300))
    fileName = db.Column(db.String(128))

    def __init__ (self, title, numBedrms, numBathrms, location, price, propType, description, fileName):
        self.title = title
        self.numBedrms = numBedrms
        self.numBathrms = numBathrms
        self.location = location
        self.price = price
        self.propType = propType
        self.description = description
        self.fileName = fileName
    
    def __repr__(self):
        return '<Property %r>' % (self.title)