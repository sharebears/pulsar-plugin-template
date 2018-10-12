from werkzeug import find_modules, import_string

from plugin_name import routes

PERMISSIONS = [
    ]


def init_app(app):
    with app.app_context():
        for name in find_modules('plugin_name', recursive=True):
            import_string(name)
        app.register_blueprint(routes.bp)
