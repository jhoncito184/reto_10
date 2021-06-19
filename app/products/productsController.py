from app import db, app
from app.products.productsModel import ProductsModel
from flask import redirect, url_for, flash
from uuid import uuid4
from werkzeug.utils import secure_filename
from os import path
from sqlalchemy.sql import func
from flask_login import current_user



class ProductsController:
    def records(self, **kwargs):
        query_api = ProductsModel.query

        if kwargs['search']:
            query_api = query_api.filter(ProductsModel.nombres.ilike(f'%{kwargs["search"]}%'))

        if kwargs['category']:
            query_api = query_api.filter_by(category_id=kwargs['category'])

        query_api = query_api.order_by(ProductsModel.id).paginate(
            page=kwargs['page'], per_page=5
        )
        return query_api

    def create(self, form, image):
        try:
            product = ProductsModel(
                                        category_id=form.category_id.data,
                                        nombres=form.nombres.data,
                                        descripcion=form.descripcion.data,
                                        precio=form.precio.data,
                                        status=1)
            db.session.add(product)
            db.session.commit()
            flash('Se creo el producto con exito !', category='success')
            return redirect(url_for('product'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('product_create'))

    def update(self, form, image, product_id):
        try:

            product = ProductsModel.query.filter_by(id=product_id).first()
            product.nombres = form.nombres.data
            product.descripcion = form.descripcion.data
            if image and image.filename:
                product.image = image.filename
            product.category_id = form.category_id.data
            product.user_id = current_user.id
            db.session.commit()
            flash('Se actualizo el producto con exito !', category='success')
            return redirect(url_for('product'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('product_update', id=product_id))

    def delete(self, product_id):
        try:
            product = ProductsModel.query.filter_by(id=product_id).first()
            status = 0 if product.status == 1 else 1
            product.status = status
            db.session.commit()
            flash('Se cambio el estado con exito !', category='success')
            return redirect(url_for('product'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('product'))
