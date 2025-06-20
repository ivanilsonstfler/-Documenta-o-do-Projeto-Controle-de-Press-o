from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile_image = db.Column(db.String(20), nullable=False, default='default.jpg') # Novo campo
    full_name = db.Column(db.String(100), nullable=True) # Novo campo
    date_of_birth = db.Column(db.DateTime, nullable=True) # Novo campo
    weight = db.Column(db.Float, nullable=True) # Novo campo
    height = db.Column(db.Float, nullable=True) # Novo campo
    blood_type = db.Column(db.String(5), nullable=True) # Novo campo
    medicoes = db.relationship("Medicao", backref="autor", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.profile_image}', '{self.full_name}', '{self.date_of_birth}', '{self.weight}', '{self.height}', '{self.blood_type}')"

class Medicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sistolica = db.Column(db.Integer, nullable=False)
    diastolica = db.Column(db.Integer, nullable=False)
    data_medicao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    notas = db.Column(db.Text, nullable=True)
    remedios_tomados = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Medicao('{self.sistolica}/{self.diastolica}', '{self.data_medicao}', '{self.remedios_tomados}')"
