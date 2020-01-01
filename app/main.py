import os

from flask import (
    Blueprint,
    Flask,
    render_template,
)
from sqlalchemy import (
    create_engine,
)
from models import (
    Organization,
)

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')

# When deployed to App Engine, the `GAE_ENV` environment variable will be
# set to `standard`
if os.environ.get('GAE_ENV') == 'standard':
    # If deployed, use the local socket interface for accessing Cloud SQL
    db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    engine_url = 'mysql+pymysql://{0}:{1}@/{2}?unix_socket={3}'.format(
                  db_user, db_password, db_name, unix_socket)
else:
    # If running locally, use the TCP connections instead
    # Set up Cloud SQL Proxy (cloud.google.com/sql/docs/mysql/sql-proxy)
    # so that your application can use 127.0.0.1:3306 to connect to your
    # Cloud SQL instance
    host = '127.0.0.1'
    engine_url = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(
                    db_user, db_password, host, db_name)

engine = create_engine(engine_url, pool_size=3)

app = Flask(__name__)

blueprint = Blueprint('app', __name__,
                      template_folder='templates',
                      static_folder='static',
                      static_url_path='/static')

@blueprint.route('/', strict_slashes=False)
def main():
    cnx = engine.connect()
    cursor = cnx.execute('SELECT NOW() as now;')
    result = cursor.fetchall()
    current_time = result[0][0]
    cnx.close()
    return str(current_time)

@blueprint.route('/organizations', strict_slashes=False)
def organizations():
    query = Organization.query.limit(40).all()
    return render_template('organizations.html',
                           organizations=query,
                           )

if __name__ == '__main__':
    #dirpath = os.path.dirname(os.path.abspath(__file__))
    #app.config.from_pyfile(os.path.join(dirpath, 'config.py'))
    app.config['SQLALCHEMY_DATABASE_URI'] = engine_url

    from models import db
    db.init_app(app)

    app.register_blueprint(blueprint)
    app.run(host='127.0.0.1', port=8080, debug=True)
