from .main_controller import main_bp

def register_routes(app):
    app.register_blueprint(main_bp)
