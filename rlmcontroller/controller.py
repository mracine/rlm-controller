import os

from flask import (
        Blueprint, current_app, flash, g, redirect, render_template, request, url_for
)

from rlmcontroller.auth import login_required
from rlmcontroller.db import get_db
from rlmcontroller.viewers import imageviewer
from rlmcontroller.utils import json

bp = Blueprint('control', __name__)

viewer = None

@bp.route('/')
# @login_required
def index():
    # TODO: Test if logged in
    if False:
        return redirect(url_for('login'))
    else:
        return render_template('index.html')

@bp.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        # TODO: Update config
        # TODO Here is where we need to display the image
        # and return an object
        # Need to pass:
        # - config (Matrix cols, etc) (do we read in again here?)
        # - commands? (do we read in again here)
        # - file to display/resource path to file

        # TODO: Fix this to come off request
        settings = json.read_from_file(current_app.config['SETTINGS_FILE'])
        resource = os.path.join(
                current_app.config['RESOURCE_PATH'],
                settings['CURRENT']
        )

        viewer.display(resource, config=app.config)

        # Write settings back out
        json.write_to_file(current_app.config['SETTINGS_FILE'], settings)

        # TODO Is this the right way to return this to the client?
        return settings

    settings = json.read_from_file(current_app.config['SETTINGS_FILE'])
    return settings
