from app import db
from app.roles.rolesModel import RolesModel
from flask import redirect, url_for, flash



class RolesController:
    def records(self, page):
        return RolesModel.query.order_by(RolesModel.id).paginate(
            page=page, per_page=5
        )

    def create(self, form):
        try:
            name_roles = form.name.data
            roles = RolesModel(name=name_roles)
            db.session.add(roles)
            db.session.commit()
            flash(f'Se creo el impuesto {name_roles} con exito !', category='success')
            return redirect(url_for('roles'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('roles_create'))

    def update(self, form, roles_id):
        try:
            name_roles = form.name.data
            roles = RolesModel.query.filter_by(id=roles_id).first()
            roles.name = name_roles
            db.session.commit()
            flash('Se actualizo el impuesto con exito !', category='success')
            return redirect(url_for('roles'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('roles_update', id=roles_id))

    def delete(self, roles_id):
        pass
        # try:
        #     roles = RolesModel.query.filter_by(id=roles_id).first()
        #     status = 0 if roles.status == 1 else 1
        #     roles.status = status
        #     db.session.commit()
        #     flash('Se cambio el estado con exito !', category='success')
        #     return redirect(url_for('roles'))
        # except Exception as e:
        #     db.session.rollback()
        #     flash(f'Ocurrio un error -> {str(e)}', category='danger')
        #     return redirect(url_for('roles'))
