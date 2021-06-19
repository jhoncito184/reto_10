from app import db
from app.tax.taxModel import TaxModel
from flask import redirect, url_for, flash



class TaxController:
    def records(self, page):
        return TaxModel.query.order_by(TaxModel.id).paginate(
            page=page, per_page=5
        )

    def create(self, form):
        try:
            valor_tax = form.valor.data
            tax = TaxModel(valor=valor_tax, status=1)
            db.session.add(tax)
            db.session.commit()
            flash(f'Se creo el impuesto {valor_tax} con exito !', category='success')
            return redirect(url_for('tax'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('tax_create'))

    def update(self, form, tax_id):
        try:
            valor_tax = form.valor.data
            tax = TaxModel.query.filter_by(id=tax_id).first()
            tax.valor = valor_tax
            db.session.commit()
            flash('Se actualizo el impuesto con exito !', category='success')
            return redirect(url_for('tax'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('tax_update', id=tax_id))

    def delete(self, tax_id):
        try:
            tax = TaxModel.query.filter_by(id=tax_id).first()
            status = 0 if tax.status == 1 else 1
            tax.status = status
            db.session.commit()
            flash('Se cambio el estado con exito !', category='success')
            return redirect(url_for('tax'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('tax'))
