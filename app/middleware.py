from functools import wraps
from flask_login import current_user
from flask import redirect, url_for, flash


def administrator(f):
    @wraps(f)
    def access_administrator(*args, **kwargs):
        if current_user.rol_id != 1:
            flash('No eres administrador', category='warning')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return access_administrator
