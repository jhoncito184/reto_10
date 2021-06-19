from app import app
from flask import render_template, request
from flask_login import login_required
from app.product.productController import ProductController
from app.product.productForm import ProductForm
from app.product.productModel import ProductModel


@app.route('/product')
@login_required
def product():
    page = request.args.get('page', type=int, default=1)
    controller = ProductController()
    product = controller.records(page)
    return render_template('views/product/index.html', title='Producto', data=product)


@app.route('/product/create', methods=['GET', 'POST'])
@login_required
def product_create():
    form = ProductForm()
    if form.validate_on_submit():
        controller = ProductController()
        return controller.create(form)
    return render_template('views/product/forms/create.html', title='Producto - Crear', form=form)


@app.route('/product/update/<int:id>', methods=['GET', 'POST'])
@login_required
def product_update(id):
    product = ProductModel.query.get_or_404(id)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        controller = ProductController()
        return controller.update(form, id)
    return render_template('views/product/forms/update.html', 
                        title='Producto - Actualizar', form=form, product_id=product.id)

@app.route('/product/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def product_delete(id):
    controller = ProductController()
    return controller.delete(id)
