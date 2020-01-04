import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), os.pardir, os.pardir)))
from app import create_app, db
from app.models import Organization


@pytest.fixture(scope='module')
def new_organization():
    return Organization(name='Test Organization')

@pytest.fixture(scope='module')
def test_client():
    app = create_app('flask_test.cfg')

    test_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield test_client  # Allow tests to run.

    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    db.drop_all()   # Delete any existing data in the database from prior run.
    db.create_all() # Create db schema.

    db.session.add(Organization(id=1, name='Org 1'))
    db.session.add(Organization(id=2, name='Org 2'))

    db.session.commit()
