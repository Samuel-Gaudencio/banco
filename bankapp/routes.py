from flask import render_template, url_for, redirect, flash
from bankapp import app, database, bcrypt
from bankapp.models import Usuario
from flask_login import login_required, login_user, logout_user, current_user
from bankapp.forms import FormLogin, FormCriarConta, FormDepositar, FormTransferir
from datetime import datetime

@app.route("/", methods=["GET", "POST"])
def homepage():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            return redirect(url_for("dashboard", id_usuario=usuario.id))
        else:
            flash("Usuário ou senha inválidos.", "danger")

    return render_template("homepage.html", form=form_login)


@app.route("/criarconta", methods=["GET", "POST"])
def criar_conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_criarconta.email.data).first()
        if usuario == None:
            usuario = Usuario.query.filter_by(cpf=form_criarconta.cpf.data).first()
            if usuario == None:
                if form_criarconta.senha.data == form_criarconta.confirmacao_senha.data:
                    senha = bcrypt.generate_password_hash(form_criarconta.senha.data).decode('utf8')
                    usuario = Usuario(nome=form_criarconta.nome.data,
                                    sobrenome=form_criarconta.sobrenome.data,
                                    cpf=form_criarconta.cpf.data,
                                    email=form_criarconta.email.data,
                                    data_nascimento=form_criarconta.data_nascimento.data,
                                    senha=senha)
                    database.session.add(usuario)
                    database.session.commit()
                    login_user(usuario, remember=True)
                    return redirect(url_for("dashboard", id_usuario=usuario.id))
                else:
                    flash("As senhas não conferem, revise-as.", "danger")
            else:
                flash("CPF já cadastrado, faça login na sua conta.", "danger")
        else:
            flash("E-mail já cadastrado, faça login na sua conta.", "danger")
    return render_template("criarconta.html", form=form_criarconta)


@app.route("/dashboard/<id_usuario>", methods=["GET", "POST"])
@login_required
def dashboard(id_usuario):
    usuario = Usuario.query.get(int(id_usuario))
    saldo = usuario.saldo
    saldo = f'R$: {saldo:,.2f}'
    return render_template("dashboard.html", usuario=usuario, saldo=saldo)

@app.route("/depositar/<id_usuario>", methods=["GET", "POST"])
@login_required
def depositar(id_usuario):
    usuario = Usuario.query.get(int(id_usuario))
    form_depositar = FormDepositar()
    if form_depositar.validate_on_submit():
        if bcrypt.check_password_hash(usuario.senha, form_depositar.senha.data):
            valor_deposito = form_depositar.valor.data
            if valor_deposito >= 1:
                usuario.saldo += valor_deposito
                usuario.extrato += f",+ R$:{valor_deposito:,.2f} {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
                database.session.commit()
                flash("Depósito realizado com sucesso!", "success")
                return redirect(url_for('depositar', id_usuario=usuario.id))
            else:
                flash("O valor do depósito tem que ser maior que 0.", "danger")
        else:
            flash("Senha inválida.", "danger")
    return render_template("depositar.html", id_usuario=usuario.id, form=form_depositar, usuario=usuario)



@app.route("/extrato", methods=["GET", "POST"])
@login_required
def extrato():
    usuario = current_user
    extrato_formatado = usuario.extrato.replace(",", "\n")
    return render_template("extrato.html", usuario=usuario, extrato=extrato_formatado)

@app.route("/transferencia/<id_usuario>", methods=["GET", "POST"])
@login_required
def transferencia(id_usuario):
    usuario = Usuario.query.get(int(id_usuario))
    form_tranferir = FormTransferir()
    if form_tranferir.validate_on_submit():
        usuario1 = Usuario.query.filter_by(cpf=form_tranferir.cpf1.data).first()
        if usuario1 != None:
            if bcrypt.check_password_hash(usuario.senha, form_tranferir.senha.data):
                valor_tranferencia = form_tranferir.valor.data
                if valor_tranferencia > 0:
                    if usuario.saldo >= valor_tranferencia:
                        usuario.saldo -= valor_tranferencia
                        usuario1.saldo += valor_tranferencia
                        usuario.extrato += f",- R$:{valor_tranferencia:.2f} {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
                        usuario1.extrato += f",+ R$:{valor_tranferencia:,.2f} {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
                        database.session.commit()
                        flash("Transferência realizada com sucesso!", "success")
                        return redirect(url_for('transferencia', id_usuario=usuario.id))
                    else:
                        flash("Saldo insuficiente para realizar a transferência.", "danger")
                else:
                        flash("O valor da transferência tem que ser maior que 0.", "danger")
            else:
                flash("Senha incorreta.", "danger")
        else:
            flash("CPF inválidos.", "danger")
    
    return render_template("transferencia.html", id_usuario=usuario.id, form=form_tranferir, usuario=usuario)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))