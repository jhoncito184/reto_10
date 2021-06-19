from app import app
from flask_login import current_user, login_required
from flask import request, render_template
from app.publications.publicationsController import PublicationsController
from app.publications.publicationsForm import PublicationsForm
from app.categories.categoriesController import CategoriesController
from app.publications.publicationsModel import PublicationsModel



@app.route('/publications')
@login_required
def publications():
    page = request.args.get('page', type=int, default=1)
    search = request.args.get('search', type=str, default='')
    category = request.args.get('category', type=int, default='')
    categories = CategoriesController.get_all()
    controller = PublicationsController()
    publications = controller.records(page=page, 
                        search=search, category=category)
    return render_template('views/publications/index.html', 
                        title='Publicaciones', 
                        data=publications, 
                        categories=categories)


@app.route('/publications/create', methods=['GET', 'POST'])
@login_required
def publications_create():
    form = PublicationsForm()
    # Get Categories
    categories = CategoriesController.get_all() # [(id, nombre)]
    form.category_id.choices = [(c.id, c.name) for c in categories]
    # End Get Categories
    if form.validate_on_submit():
        controller = PublicationsController()
        image = request.files['image']
        return controller.create(form, image)
    return render_template('views/publications/forms/create.html', 
                        title='Publicaciones - Crear', form=form)


@app.route('/publications/update/<int:id>', methods=['GET', 'POST'])
@login_required
def publications_update(id):
    publication = PublicationsModel.query.get_or_404(id)
    form = PublicationsForm(obj=publication)
    # Get Categories
    categories = CategoriesController.get_all() # [(id, nombre)]
    form.category_id.choices = [(c.id, c.name) for c in categories]
    # End Get Categories
    if form.validate_on_submit():
        controller = PublicationsController()
        image = request.files['image']
        form.image_old = request.form['image_old']
        return controller.update(form, image, id)
    return render_template('views/publications/forms/update.html', 
                        title='Publicaciones - Actualizar', form=form, publication_id=publication.id)


@app.route('/publications/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def publications_delete(id):
    controller = PublicationsController()
    return controller.delete(id)
