from flask import render_template

from app.models import (
    Organization,
    OrganizationRole,
    User,
)

from . import admin_blueprint


@admin_blueprint.route('/organizations', strict_slashes=False)
def organizations():
    query = Organization.query.order_by(Organization.name).limit(40)
    return render_template('admin/organizations.html', organizations=query)

@admin_blueprint.route('/organization/<organization_id>', strict_slashes=False)
def organization(organization_id):
    org = Organization.query.filter(Organization.id == organization_id).first()
    user_count = OrganizationRole.query.filter(OrganizationRole.organization_id
            == organization_id).count()
    return render_template('admin/organization.html',
            title=org.name,
            organization_id=organization_id,
            user_count=user_count)

@admin_blueprint.route('/organization/<organization_id>/<what>',
        strict_slashes=False)
def organization_users(organization_id, what):
    org = Organization.query.filter(Organization.id == organization_id).first()
    if what == 'users':
        users = User.query.join(
                User.organization_roles).filter_by(
                        organization_id=org.id).limit(40)
        return render_template('admin/organization_users.html',
                title='{} Users'.format(org.name),
                users=users)

@admin_blueprint.route('/user/<user_id>', strict_slashes=False)
def user(user_id):
    user = User.query.filter(User.id == user_id).first()
    return render_template('admin/user.html',
            title=user.name)
