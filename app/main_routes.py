from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
from app import db
from app.forms import MedicaoForm, ProfileForm
from app.models import Medicao, User
from flask_login import current_user, login_required
from datetime import datetime, timedelta
import os
import secrets
from PIL import Image

main = Blueprint("main", __name__)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(main.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@main.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    form = MedicaoForm()
    if form.validate_on_submit():
        medicao = Medicao(sistolica=form.sistolica.data, diastolica=form.diastolica.data, 
                          notas=form.notas.data, remedios_tomados=form.remedios_tomados.data, autor=current_user)
        db.session.add(medicao)
        db.session.commit()
        flash("Medição adicionada com sucesso!", "success")
        return redirect(url_for("main.dashboard"))
    
    # Fetch measurements for the current user
    medicoes = Medicao.query.filter_by(user_id=current_user.id).order_by(Medicao.data_medicao.desc()).all()
    
    # Prepare data for chart
    labels = [m.data_medicao.strftime("%d/%m/%Y %H:%M") for m in medicoes]
    sistolicas = [m.sistolica for m in medicoes]
    diastolicas = [m.diastolica for m in medicoes]

    return render_template("dashboard.html", title="Dashboard", form=form, medicoes=medicoes,
                           labels=labels, sistolicas=sistolicas, diastolicas=diastolicas)

@main.route("/get_medicoes", methods=["GET"])
@login_required
def get_medicoes():
    start_date_str = request.args.get("start_date")
    end_date_str = request.args.get("end_date")

    query = Medicao.query.filter_by(user_id=current_user.id)

    if start_date_str:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        query = query.filter(Medicao.data_medicao >= start_date)
    if end_date_str:
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d") + timedelta(days=1) - timedelta(microseconds=1) # Include full end day
        query = query.filter(Medicao.data_medicao <= end_date)

    medicoes = query.order_by(Medicao.data_medicao.desc()).all()

    medicoes_data = []
    for m in medicoes:
        status = "Normal"
        if m.sistolica >= 140 or m.diastolica >= 90:
            status = "Hipertensão Estágio 2"
        elif m.sistolica >= 130 or m.diastolica >= 80:
            status = "Hipertensão Estágio 1"
        elif m.sistolica >= 120 and m.diastolica < 80:
            status = "Elevada"

        medicoes_data.append({
            "id": m.id,
            "sistolica": m.sistolica,
            "diastolica": m.diastolica,
            "data_medicao": m.data_medicao.strftime("%d/%m/%Y %H:%M"),
            "notas": m.notas,
            "remedios_tomados": m.remedios_tomados,
            "status": status
        })
    return jsonify(medicoes_data)

@main.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        if form.profile_image.data:
            picture_file = save_picture(form.profile_image.data)
            current_user.profile_image = picture_file
        current_user.full_name = form.full_name.data
        current_user.date_of_birth = form.date_of_birth.data
        current_user.weight = form.weight.data
        current_user.height = form.height.data
        current_user.blood_type = form.blood_type.data
        db.session.commit()
        flash("Seu perfil foi atualizado com sucesso!", "success")
        return redirect(url_for("main.profile"))
    elif request.method == "GET":
        form.full_name.data = current_user.full_name
        form.date_of_birth.data = current_user.date_of_birth
        form.weight.data = current_user.weight
        form.height.data = current_user.height
        form.blood_type.data = current_user.blood_type
    image_file = url_for("static", filename="profile_pics/" + current_user.profile_image)
    return render_template("profile.html", title="Perfil", image_file=image_file, form=form)
