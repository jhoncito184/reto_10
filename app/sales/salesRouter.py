from app import app
from flask import render_template, request
from flask_login import login_required
from app.sales.salesController import SalesController
# from app.sales.salesForm import SalesForm
from app.sales.salesModel import SalesModel


@app.route('/sales')
@login_required
def sales():
    page = request.args.get('page', type=int, default=1)
    controller = SalesController()
    sales = controller.records(page)
    return render_template('views/sales/index.html', title='Ventas', data=sales)