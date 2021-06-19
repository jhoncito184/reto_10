from app import app
from flask import render_template, request
from flask_login import login_required
from app.salesType.salesTypeController import SalesTypeController
from app.salesType.salesTypeForm import SalesTypeForm
from app.salesType.salesTypeModel import SalesTypeModel


@app.route('/salesType')
@login_required
def salesType():
    page = request.args.get('page', type=int, default=1)
    controller = SalesTypeController()
    salesType = controller.records(page)
    return render_template('views/salesType/index.html', title='Tipo de venta', data=salesType)


@app.route('/salesType/create', methods=['GET', 'POST'])
@login_required
def salesType_create():
    form = SalesTypeForm()
    if form.validate_on_submit():
        controller = SalesTypeController()
        return controller.create(form)
    return render_template('views/salesType/forms/create.html', title='Tipo de venta - Crear', form=form)


@app.route('/salesType/update/<int:id>', methods=['GET', 'POST'])
@login_required
def salesType_update(id):
    salesType = SalesTypeModel.query.get_or_404(id)
    form = SalesTypeForm(obj=salesType)
    if form.validate_on_submit():
        controller = SalesTypeController()
        return controller.update(form, id)
    return render_template('views/salesType/forms/update.html', 
                        title='Tipo de venta - Actualizar', form=form, salesType_id=salesType.id)

@app.route('/salesType/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def salesType_delete(id):
    controller = SalesTypeController()
    return controller.delete(id)
