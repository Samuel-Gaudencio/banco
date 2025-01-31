from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, FloatField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError, Email
from bankapp.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    botao_confirmacao = SubmitField("Fazer Login")

class FormCriarConta(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    sobrenome = StringField("Sobrenome", validators=[DataRequired()])
    cpf = StringField("CPF", validators=[DataRequired(), Length(11, 14)])
    data_nascimento = DateField("Data de Nascimento", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Criar Conta")


class FormDepositar(FlaskForm):
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    valor = FloatField("Valor", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Depositar")

class FormTransferir(FlaskForm):
    cpf1 = StringField("CPF do Destinatário", validators=[DataRequired(), Length(11, 14)])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    valor = FloatField("Valor", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Transferir")