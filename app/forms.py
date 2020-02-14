from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length


class RegisterForm(Form):
    name = StringField("Nome", validators=[
        DataRequired("Campo obrigatório!"),
        Length(5, 100, "O campo deve possuir entre 5 e 100 caracteres")
    ])
    email = StringField("E-mail", validators=[
        DataRequired("Campo obrigatório!"),
        Email('não é um e-mail válido'),
        Length(5, 100, "O campo deve possuir entre 5 e 100 caracteres")
    ])
    password = PasswordField("Senha", validators=[
        DataRequired("Campo obrigatório!")
    ])
    submit = SubmitField("Cadastrar")

class LoginForm(Form):
    email = StringField("E-mail", validators=[
        DataRequired("Campo obrigatório!"),
        Email('não é um e-mail válido')
    ])
    password = PasswordField("Senha", validators=[
        DataRequired("Campo obrigatório!")
    ])
    submit = SubmitField("Cadastrar")