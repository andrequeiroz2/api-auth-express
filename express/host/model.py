from express.database import db

class Host(db.Model):
    __tablename__ = "host"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(120), index=True, nullable=False)
    