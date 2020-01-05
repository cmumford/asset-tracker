import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    if not 'SQLALCHEMY_DATABASE_URI' in app.config:
        db_user = os.environ.get('CLOUD_SQL_USERNAME')
        db_password = os.environ.get('CLOUD_SQL_PASSWORD')
        db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')

        # When deployed to App Engine, the `GAE_ENV` environment variable will
        # be set to `standard`
        if os.environ.get('GAE_ENV') == 'standard':
            # If deployed, use the local socket interface for accessing Cloud
            # SQL.
            db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
            unix_socket = '/cloudsql/{}'.format(db_connection_name)
            database_uri = 'mysql+pymysql://{0}:{1}@/{2}?unix_socket={3}'.format(
                    db_user, db_password, db_name, unix_socket)
        else:
            # If running locally, use the TCP connections instead
            # Set up Cloud SQL Proxy (cloud.google.com/sql/docs/mysql/sql-proxy)
            # so that your application can use 127.0.0.1:3306 to connect to your
            # Cloud SQL instance
            host = '127.0.0.1'
            database_uri = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(
                    db_user, db_password, host, db_name)
        app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

    initialize_extensions(app)
    register_blueprints(app)

    if True:
        # Creating test for easy development. Delete for deployment.
        from app.tests import conftest
        with app.app_context():
            conftest.make_test_data()

    return app

def initialize_extensions(app):
    db.init_app(app)

def register_blueprints(app):
    from app.main import main_blueprint
    from app.admin import admin_blueprint

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(main_blueprint)
