from app import db
from app.product.productModel import ProductModel
from flask import redirect, url_for, flash



class ProductController:
    def records(self, page):
        return ProductModel.query.order_by(ProductModel.id).paginate(
            page=page, per_page=5
        )

    def create(self, form):
        try:
            name_product = form.name.data
            product = ProductModel(name=name_product, status=1)
            db.session.add(product)
            db.session.commit()
            flash(f'Se creo el producto {name_product} con exito !', category='success')
            return redirect(url_for('product'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('product_create'))

    def update(self, form, product_id):
        try:
            name_product = form.name.data
            product = ProductModel.query.filter_by(id=product_id).first()
            product.name = name_product
            db.session.commit()
            flash('Se actualizo el producto con exito !', category='success')
            return redirect(url_for('product'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('product_update', id=product_id))

    def delete(self, product_id):
        try:
            product = ProductModel.query.filter_by(id=product_id).first()
            status = 0 if product.status == 1 else 1
            product.status = status
            db.session.commit()
            flash('Se cambio el estado con exito !', category='success')
            return redirect(url_for('product'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('product'))
