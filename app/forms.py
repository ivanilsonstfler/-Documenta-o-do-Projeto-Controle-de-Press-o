from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, DateField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange, Optional
from flask_wtf.file import FileField, FileAllowed
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField("Nome de Usuário",
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email",
                        validators=[DataRequired(), Email(), Length(min=6, max=120)])
    password = PasswordField("Senha", validators=[DataRequired(), Length(min=6, max=60)])
    confirm_password = PasswordField("Confirmar Senha",
                                     validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Cadastrar")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Esse nome de usuário já está em uso. Por favor, escolha outro.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Esse email já está em uso. Por favor, escolha outro.")

class LoginForm(FlaskForm):
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Login")

class MedicaoForm(FlaskForm):
    sistolica = IntegerField("Pressão Sistólica", validators=[DataRequired(), NumberRange(min=50, max=300)])
    diastolica = IntegerField("Pressão Diastólica", validators=[DataRequired(), NumberRange(min=30, max=200)])
    notas = TextAreaField("Notas (opcional)", validators=[Length(max=200)])
    remedios_tomados = TextAreaField("Remédios Tomados (opcional)", validators=[Length(max=200)])
    submit = SubmitField("Adicionar Medição")

class ProfileForm(FlaskForm):
    full_name = StringField("Nome Completo", validators=[Optional(), Length(max=100)])
    date_of_birth = DateField("Data de Nascimento (AAAA-MM-DD)", format="%Y-%m-%d", validators=[Optional()])
    weight = FloatField("Peso (kg)", validators=[Optional(), NumberRange(min=0)])
    height = FloatField("Altura (cm)", validators=[Optional(), NumberRange(min=0)])
    blood_type = StringField("Tipo Sanguíneo", validators=[Optional(), Length(max=5)])
    profile_image = FileField("Foto de Perfil", validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField("Atualizar Perfil")
