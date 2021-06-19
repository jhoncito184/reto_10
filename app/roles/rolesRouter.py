from app import app
from flask import render_template, request
from flask_login import login_required
from app.roles.rolesController import RolesController
from app.roles.rolesForm import RolesForm
from app.roles.rolesModel import RolesModel


@app.route('/roles')
@login_required
def roles():
    page = request.args.get('page', type=int, default=1)
    controller = RolesController()
    roles = controller.records(page)
    return render_template('views/roles/index.html', title='Tipo de usuarios', data=roles)


@app.route('/roles/create', methods=['GET', 'POST'])
@login_required
def roles_create():
    form = RolesForm()
    if form.validate_on_submit():
        controller = RolesController()
        return controller.create(form)
    return render_template('views/roles/forms/create.html', title='Tipo de usuarios - Crear', form=form)


@app.route('/roles/update/<int:id>', methods=['GET', 'POST'])
@login_required
def roles_update(id):
    roles = RolesModel.query.get_or_404(id)
    form = RolesForm(obj=roles)
    if form.validate_on_submit():
        controller = RolesController()
        return controller.update(form, id)
    return render_template('views/roles/forms/update.html', 
                        title='Tipo de usuarios - Actualizar', form=form, roles_id=roles.id)

@app.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def roles_delete(id):
    controller = RolesController()
    return controller.delete(id)
