from app import app
from flask import render_template, request
from flask_login import login_required
from app.tax.taxController import TaxController
from app.tax.taxForm import TaxForm
from app.tax.taxModel import TaxModel


@app.route('/tax')
@login_required
def tax():
    page = request.args.get('page', type=int, default=1)
    controller = TaxController()
    tax = controller.records(page)
    return render_template('views/tax/index.html', title='Impuestos', data=tax)


@app.route('/tax/create', methods=['GET', 'POST'])
@login_required
def tax_create():
    form = TaxForm()
    if form.validate_on_submit():
        controller = TaxController()
        return controller.create(form)
    return render_template('views/tax/forms/create.html', title='Impuestos - Crear', form=form)


@app.route('/tax/update/<int:id>', methods=['GET', 'POST'])
@login_required
def tax_update(id):
    tax = TaxModel.query.get_or_404(id)
    form = TaxForm(obj=tax)
    if form.validate_on_submit():
        controller = TaxController()
        return controller.update(form, id)
    return render_template('views/tax/forms/update.html', 
                        title='Impuestos - Actualizar', form=form, tax_id=tax.id)

@app.route('/tax/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def tax_delete(id):
    controller = TaxController()
    return controller.delete(id)
