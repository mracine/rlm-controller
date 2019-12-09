import os

from flask import Flask
from rlmcontroller.utils import json, path
from rlmcontroller.viewers.imageviewer import ImageViewer

# App factory
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'rlmcontroller.sqlite'),
    )

    # TODO: Need to read potential instance_path from command line
    # else default to regular instance

    try:
        os.makedirs(app.instance_path, exist_ok=True)

        # Load in app config
        if test_config is None:
            config_path = os.path.join(app.instance_path, 'config.json')
            
            # Fallback to default config
            if not os.path.exists(config_path):
                app.config.from_object('rlmcontroller.config.config.Config')

            app.config.from_json(config_path)
        else:
            app.config.from_mapping(test_config)

        # Resource dirs for images/videos to display
        resources_dir = path.get_absolute_dirname(app.config['RESOURCE_PATH'], app.instance_path)
        if not os.path.exists(resources_dir):
            os.makedirs(resources_dir)

    except OSError:
        pass

    # TODO May not have to do this, check out app.open_instance_resource(filename)
    app.config["COMMANDS_FILE"] = os.path.join(app.instance_path, "commands.json")
    app.config["SETTINGS_FILE"] = os.path.join(app.instance_path, ".settings.json")

    # TODO Maybe?
    # app.config['CONFIG'] = json.json_to_dict()
    # app.config['COMMANDS'] = json.json_to_dict()
    # app.config['SETTINGS'] = json.json_to_dict()

    from . import db
    db.init_app(app)

    from . import auth, controller
    app.register_blueprint(auth.bp)
    app.register_blueprint(controller.bp)
    app.add_url_rule('/', endpoint='index')

    # TODO best way to handle this
    controller.viewer = ImageViewer()

    # Turn on device if it was last on when the app shutdown
    if json.read_from_file(app.config['SETTINGS_FILE'])['ON']:
        # TODO Actually turn device on
        controller.viewer.display(
                os.path.join(
                    app.config['RESOURCE_PATH'],
                    json.read_from_file(app.config['SETTINGS_FILE'])['CURRENT']
                ),
                config=app.config
        )
        pass

    return app
