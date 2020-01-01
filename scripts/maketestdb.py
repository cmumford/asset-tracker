#!/usr/bin/env python3

import os
import random
import sys
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), os.pardir)))

from app.models import (
  Role,
)

def getdburl():
    hostname = 'localhost'
    username = 'asset-web'
    password = 'password'
    dbname = 'easy_asset_tracker'
    return 'mysql+pymysql://{}:{}@{}/{}'.format(
            username, password, hostname, dbname)

def CreateRoles(metadata, connection):
    role_table = Table('role', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(80)),
                    )
    roles = [
        {'id': 0, 'name': 'Super Administrator'},
        {'id': 1, 'name': 'Administrator'},
        {'id': 2, 'name': 'Standard user'},
        {'id': 3, 'name': 'Read-only'},
    ]
    for role in roles:
        ins = role_table.insert()
        new_role = ins.values(id=role['id'], name=role['name'])
        connection.execute(new_role)

def CreateUsers(metadata, connection):
    user_table = Table('user', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(80)),
                    Column('role_id', Integer),
                    Column('organization_id', Integer),
                    )
    users = [
        {'id': 1, 'name': 'root', 'role_id': 0, 'organization_id': 0},
        {'id': 2, 'name': 'admin', 'role_id': 1, 'organization_id': 1},
        {'id': 3, 'name': 'std-user', 'role_id': 2, 'organization_id': 1},
        {'id': 4, 'name': 'guest 1', 'role_id': 3, 'organization_id': 1},
        {'id': 5, 'name': 'guest 2', 'role_id': 3, 'organization_id': 1},
    ]
    for user in users:
        ins = user_table.insert()
        new_user = ins.values(id=user['id'],
                              name=user['name'],
                              role_id=user['role_id'],
                              organization_id=user['organization_id'],
                              )
        connection.execute(new_user)

def CreateAssetTypes(metadata, connection):
    table = Table('asset_type', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(80)),
                    Column('organization_id', Integer),
                    )
    items = [
        {'id': 1, 'name': 'Violin', 'organization_id': 1},
        {'id': 2, 'name': 'Viola', 'organization_id': 1},
        {'id': 3, 'name': 'Cello', 'organization_id': 1},
    ]
    for item in items:
        ins = table.insert()
        new_item = ins.values(id=item['id'],
                              name=item['name'],
                              organization_id=item['organization_id'],
                              )
        connection.execute(new_item)

def CreateManufacturers(metadata, connection):
    table = Table('manufacturer', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(256)),
                    Column('organization_id', Integer),
                    )
    items = [
        {'id': 1, 'name': 'Stradivarius', 'organization_id': 1},
        {'id': 2, 'name': 'Guarneri', 'organization_id': 1},
        {'id': 3, 'name': 'Eugenio Degani', 'organization_id': 1},
    ]
    for item in items:
        ins = table.insert()
        new_item = ins.values(id=item['id'],
                              name=item['name'],
                              organization_id=item['organization_id'],
                              )
        connection.execute(new_item)

def CreateAssets(metadata, connection):
    table = Table('asset', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('asset_id', Integer),
                    Column('asset_type_id', Integer),
                    Column('name', String(80)),
                    Column('manufacturer_id', Integer),
                    Column('organization_id', Integer),
                    )
    next_id = 0
    next_asset_id = 1
    categories = [
            {'name': 'Violin', 'asset_type_id': 1, 'organization_id': 1},
            {'name': 'Viola', 'asset_type_id': 2, 'organization_id': 1},
            {'name': 'Cello', 'asset_type_id': 3, 'organization_id': 1},
    ]
    for idx in range(50):
        for category in categories:
            ins = table.insert()
            name = '{0} #{1}'.format(category['name'], idx+1)
            new_item = ins.values(id=next_id,
                                  name=name,
                                  asset_id=next_asset_id,
                                  asset_type_id=category['asset_type_id'],
                                  manufacturer_id=random.randint(1, 3),
                                  organization_id=category['organization_id'],
                                  )
            connection.execute(new_item)
            next_asset_id += 1
            next_id += 1

def CreateAssignees(metadata, connection):
    table = Table('assignee', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(256)),
                    Column('asset_id', Integer),
                    Column('organization_id', Integer),
                    )
    items = [
        {'id': 1, 'name': 'Joe Smith', 'organization_id': 1},
        {'id': 2, 'name': 'Joe Clark', 'organization_id': 1},
        {'id': 3, 'name': 'Mary Rogers', 'organization_id': 1},
        {'id': 4, 'name': 'Patty Bush', 'organization_id': 1},
    ]
    for item in items:
        ins = table.insert()
        new_item = ins.values(id=item['id'],
                              name=item['name'],
                              organization_id=item['organization_id'],
                              )
        connection.execute(new_item)

def CreateOrganizations(metadata, connection):
    table = Table('organization', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(256)),
                    )
    items = [
        {'id': 0, 'name': 'Hosting'},
        {'id': 1, 'name': 'Summerville High School'},
        {'id': 2, 'name': 'Gunn High School'},
        {'id': 3, 'name': 'Palo Alto High School'},
    ]
    for item in items:
        ins = table.insert()
        new_item = ins.values(id=item['id'], name=item['name'])
        connection.execute(new_item)

def MapAssignees(metadata, connection):
    table = Table('assignee_asset', metadata,
                    Column('assignee_id', Integer),
                    Column('asset_id', Integer),
                    )
    items = [
        {'assignee_id': 1, 'asset_id': 1},
        {'assignee_id': 1, 'asset_id': 2},
        {'assignee_id': 4, 'asset_id': 19},
    ]
    for item in items:
        ins = table.insert()
        new_item = ins.values(assignee_id=item['assignee_id'],
                              asset_id=item['asset_id'])
        connection.execute(new_item)

if __name__ == '__main__':
    db = create_engine(getdburl())
    metadata = MetaData(bind=db)

    connection = db.connect()
    CreateOrganizations(metadata, connection)
    CreateRoles(metadata, connection)
    CreateUsers(metadata, connection)
    CreateAssetTypes(metadata, connection)
    CreateManufacturers(metadata, connection)
    CreateAssets(metadata, connection)
    CreateAssignees(metadata, connection)
    MapAssignees(metadata, connection)
