import os
from flask import Flask


def create_app(script_info=None):
    app = Flask(__name__)
        
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    
    from app.jobs.routes import jobs_blueprint
    app.register_blueprint(jobs_blueprint, url_prefix="/jobs")
    
    app.shell_context_processor({ "app": app })
    
    return app