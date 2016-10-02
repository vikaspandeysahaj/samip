import os

from config.config_loader import samip_config
from samip.application import create_app


from samip.blueprints import register_blueprints
from samip.db_storage import storage


def devserver():
    config = samip_config.load()
    app = create_app(config)
    register_blueprints(app)
    storage.init_storage(app.config)
    app.run(host='0.0.0.0', port=6060)

devserver()
