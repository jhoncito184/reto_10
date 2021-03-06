from app import app
from flask_login import current_user, login_required
from flask import request, render_template
from app.products.productsController import ProductsController
from app.products.productsForm import ProductsForm
from app.categories.categoriesController import CategoriesController
from app.products.productsModel import ProductsModel



@app.route('/products')
@login_required
def products():
    page = request.args.get('page', type=int, default=1)
    search = request.args.get('search', type=str, default='')
    category = request.args.get('category', type=int, default='')
    categories = CategoriesController.get_all()
    controller = ProductsController()
    products = controller.records(page=page, 
                        search=search, category=category)
    return render_template('views/products/index.html', 
                        title='Productos', 
                        data=products, 
                        categories=categories)


@app.route('/products/create', methods=['GET', 'POST'])
@login_required
def products_create():
    form = ProductsForm()
    # Get Categories
    categories = CategoriesController.get_all() # [(id, nombre)]
    form.category_id.choices = [(c.id, c.name) for c in categories]
    # End Get Categories
    if form.validate_on_submit():
        controller = ProductsController()
        return controller.create(form)
    return render_template('views/products/forms/create.html', 
                        title='Productos - Crear', form=form)


@app.route('/products/update/<int:id>', methods=['GET', 'POST'])
@login_required
def products_update(id):
    product = ProductsModel.query.get_or_404(id)
    form = ProductsForm(obj=product)
    # Get Categories
    categories = CategoriesController.get_all() # [(id, nombre)]
    form.category_id.choices = [(c.id, c.name) for c in categories]
    # End Get Categories
    if form.validate_on_submit():
        controller = ProductsController()
        return controller.update(form, id)
    return render_template('views/products/forms/update.html', 
                        title='Productos - Actualizar', form=form, product_id=product.id)


@app.route('/products/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def products_delete(id):
    controller = ProductsController()
    return controller.delete(id)
