from app import db, app
from app.sales.salesModel import SalesModel
from flask import redirect, url_for, flash
from uuid import uuid4
from werkzeug.utils import secure_filename
from os import path
from sqlalchemy.sql import func
from flask_login import current_user



class SalesController:
    def records(self, **kwargs):
        query_api = SalesModel.query

        if kwargs['search']:
            query_api = query_api.filter(SalesModel.total.ilike(f'%{kwargs["search"]}%'))

        query_api = query_api.order_by(SalesModel.id).paginate(
            page=kwargs['page'], per_page=5
        )
        return query_api
