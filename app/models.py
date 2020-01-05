from app import db

class Organization(db.Model):
    __tablename__ = 'organization'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

association_table = db.Table('organization_role_user_association',
        db.Model.metadata,
    db.Column('organization_role_id', db.Integer,
        db.ForeignKey('organization_role.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class OrganizationRole(db.Model):
    __tablename__ = 'organization_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    organization_id = db.Column(db.ForeignKey('organization.id'),
            nullable=False)
    organization = db.relationship('Organization')
    role_id = db.Column(db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role')
    users = db.relationship('User',
            secondary=association_table, back_populates='organization_roles')

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    organization_roles = db.relationship('OrganizationRole',
            secondary=association_table, back_populates='users')

class AssetType(db.Model):
    __tablename__ = 'asset_type'
    organization_id = db.Column(db.ForeignKey('organization.id'),
            nullable=False)
    organization = db.relationship('Organization')
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)

class Manufacturer(db.Model):
    __tablename__ = 'manufacturer'
    organization_id = db.Column(db.ForeignKey('organization.id'),
            nullable=False)
    organization = db.relationship('Organization')
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)

class Assignee(db.Model):
    __tablename__ = 'assignee'
    organization_id = db.Column(db.ForeignKey('organization.id'),
            nullable=False)
    organization = db.relationship('Organization')
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=True)

class Asset(db.Model):
    __tablename__ = 'asset'
    organization_id = db.Column(db.ForeignKey('organization.id'),
            nullable=False)
    organization = db.relationship('Organization')
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    asset_type_id = db.Column(db.ForeignKey('asset_type.id'), nullable=False)
    asset_type = db.relationship('AssetType')
    asset_id = db.Column(db.Integer, nullable=True)
    manufacturer_id = db.Column(db.ForeignKey('manufacturer.id'), nullable=True)
    manufacturer = db.relationship('Manufacturer')
    assignee_id = db.Column(db.ForeignKey('assignee.id'), nullable=False)
    assignee = db.relationship('Assignee')
