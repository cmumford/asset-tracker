from flask import render_template

from app.models import (
    Organization,
)

from . import admin_blueprint


@admin_blueprint.route('/organizations', strict_slashes=False)
def organizations():
    query = Organization.query.order_by(Organization.name).limit(40)
    return render_template('admin/organizations.html', organizations=query)

@admin_blueprint.route('/organization/<organization_id>', strict_slashes=False)
def organization(organization_id):
    org = Organization.query.filter(Organization.id == organization_id).first()
    return render_template('admin/organization.html', title=org.name)