from app import db
from app.categories.categoriesModel import CategoriesModel
from flask import redirect, url_for, flash



class CategoriesController:
    def records(self, **kwargs):
        query_api = CategoriesModel.query

        if kwargs['search']:
            query_api = query_api.filter(CategoriesModel.name.ilike(f'%{kwargs["search"]}%'))

        query_api = query_api.order_by(CategoriesModel.id).paginate(
            page=kwargs['page'], per_page=5
        )
        return query_api

    def create(self, form):
        try:
            name_category = form.name.data
            category = CategoriesModel(name=name_category, status=1) # objeto nuevo
            db.session.add(category)
            db.session.commit()
            flash(f'Se creo la categoria {name_category} con exito !', category='success')
            return redirect(url_for('categories'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('categories_create'))

    def update(self, form, category_id):
        try:
            name_category = form.name.data
            category = CategoriesModel.query.filter_by(id=category_id).first() # objeto existente
            category.name = name_category
            db.session.commit()
            flash('Se actualizo la categoria con exito !', category='success')
            return redirect(url_for('categories'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('categories_update', id=category_id))

    def delete(self, category_id):
        try:
            category = CategoriesModel.query.filter_by(id=category_id).first()
            status = 0 if category.status == 1 else 1
            category.status = status
            db.session.commit()
            flash('Se cambio el estado con exito !', category='success')
            return redirect(url_for('categories'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('categories'))

    @staticmethod
    def get_all():
        return CategoriesModel.query.filter_by(status=1)\
            .order_by(CategoriesModel.name).all()