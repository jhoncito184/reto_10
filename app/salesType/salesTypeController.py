from app import db
from app.salesType.salesTypeModel import SalesTypeModel
from flask import redirect, url_for, flash



class SalesTypeController:
    def records(self, page):
        return SalesTypeModel.query.order_by(SalesTypeModel.id).paginate(
            page=page, per_page=5
        )

    def create(self, form):
        try:
            name_salesType = form.name.data
            salesType = SalesTypeModel(name=name_salesType)
            db.session.add(salesType)
            db.session.commit()
            flash(f'Se creo el impuesto {name_salesType} con exito !', category='success')
            return redirect(url_for('salesType'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('salesType_create'))

    def update(self, form, salesType_id):
        try:
            name_salesType = form.name.data
            salesType = SalesTypeModel.query.filter_by(id=salesType_id).first()
            salesType.name = name_salesType
            db.session.commit()
            flash('Se actualizo el impuesto con exito !', category='success')
            return redirect(url_for('salesType'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('salestype_update', id=salesType_id))

    def delete(self, salesType_id):
        pass
        # try:
        #     salesType = SalesTypeModel.query.filter_by(id=salesType_id).first()
        #     status = 0 if salesType.status == 1 else 1
        #     salesType.status = status
        #     db.session.commit()
        #     flash('Se cambio el estado con exito !', category='success')
        #     return redirect(url_for('salesType'))
        # except Exception as e:
        #     db.session.rollback()
        #     flash(f'Ocurrio un error -> {str(e)}', category='danger')
        #     return redirect(url_for('salestype'))
