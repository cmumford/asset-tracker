import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), os.pardir, os.pardir)))
from app import create_app, db
from app.models import (
        Asset,
        AssetType,
        Assignee,
        Manufacturer,
        Organization,
        OrganizationRole,
        Role,
        User,
)


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
    db.create_all() # Create db tables.

    org_names = [
        'Gunn High School',
        'Palo Alto High School',
        'Summerville High School',
    ]

    role_names = [
        'Super Administrator',
        'Administrator',
        'Standard',
        'Read only',
    ]

    instrument_types = [
        'Cello',
        'Double Bass',
        'Viola',
        'Violin',
    ]

    user_names = [
        'Barbara Jones',
        'Richard Clark',
        'Joe Smith',
        'Sarah Parker',
    ]

    assignee_names = [
        'Student 1',
        'Student 2',
        'Student 3',
        'Student 4',
        'Student 5',
        'Student 6',
    ]

    #################
    # Roles
    #################
    roles = [Role(name=n) for n in role_names]
    for role in roles:
        db.session.add(role)

    #################
    # Users
    #################
    users = [User(name=n) for n in user_names]
    for user in users:
        db.session.add(user)

    for org_name in org_names:
        #################
        # Organizations
        #################
        organization = Organization(name=org_name)
        db.session.add(organization)

        ####################
        # OrginizationRoles
        ####################
        org_roles = [OrganizationRole(organization=organization, role=r)
                for r in roles]
        for role in org_roles:
            db.session.add(role)

        # First user is an admin of all orgs.
        users[0].organization_roles.append(org_roles[1])
        # Second user is a standard member of all orgs.
        users[1].organization_roles.append(org_roles[2])
        # Third user is a read-only member of all orgs.
        users[2].organization_roles.append(org_roles[3])

        #################
        # Assignees
        #################
        band_room = Assignee(organization=organization,
                name='{} Band Room'.format(organization.name))
        assignees = [band_room] + [Assignee(organization=organization, name=n)
                for n in assignee_names]
        for assignee in assignees:
            db.session.add(assignee)

        #################
        # AssetType
        #################
        asset_types = [AssetType(organization=organization, name=n)
                for n in instrument_types]
        for asset_type in asset_types:
            db.session.add(asset_type)

        #################
        # Assets
        #################
        next_asset_id = 1
        for idx in range(50):
            type_num = 1
            for asset_type in asset_types:
                name = '{0} #{1}'.format(asset_type.name, type_num)
                asset = Asset(organization=asset_type.organization,
                        asset_type=asset_type,
                        assignee=band_room,
                        manufacturer=None,
                        name=name,
                        asset_id=next_asset_id)
                next_asset_id += 1
                type_num += 1
                db.session.add(asset)

    db.session.commit()
