from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from models import User


class RegistrationForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    email = StringField('correo electrónico ', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField(
        'Confirmar contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Enviar')

class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('correo electrónico ', validators=[DataRequired()])
    remember_me = BooleanField('Contraseña')
    submit = SubmitField('Ingresar')

class DestinationForm(FlaskForm):
    city = StringField('Ciudad')
    country = StringField('Pais')
    description = StringField('Describe el menu')
    submit = SubmitField('Publicar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('ingrese un nombre usuario diferente.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('ingrese un email diferente.')