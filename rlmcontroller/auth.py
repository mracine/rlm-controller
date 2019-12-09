import functools

from flask import (
        Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from rlmcontroller.db import get_db

bp = Blueprint('auth', __name__)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))

        return view(**kwargs)

    return wrapped_view

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db.execute(
                'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
                'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        # Could potentially split these out, but maybe the
        # ambiguity will help security
        if user or check_password_hash(user['password'], password):
            error = 'Incorrect username or password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# TODO: Page for changing password/creating new login?
# Need to make sure user has permissions, admin etc.
#@bp.route('/account', methods=['GET', 'POST'])
#def account():
#    if request.method == 'POST':
#        username = request.form['username']
#        password = request.form['password']
#        db = get_db()
#        error = None
#
#        # Note: ideally, we won't hit any of these
#        # since the frontend has its own validation
#        # Still, the extra security can't hurt
#        if not username:
#            error = 'Username is required.'
#        elif not password:
#            error = 'Password is required.'
#        elif db.execute(
#                'SELECT id FROM user WHERE username = ?', (username,)
#        ).fetchone() is not None:
#            error = 'User {} is already registered.'.format(username)
#
#        if error is None:
#            db.execute(
#                    'INSERT INTO user (username, password) VALUES (?, ?)',
#                    (username, generate_password_hash(password))
#            )
#            db.commit()
#            return redirect(url_for('login'))
#
#    return render_template('account.html')

