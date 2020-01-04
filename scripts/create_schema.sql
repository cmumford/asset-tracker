
USE easy_asset_tracker;

CREATE TABLE organization (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE role (
  id INT NOT NULL,
  name VARCHAR(80),
  PRIMARY KEY (id)
);

CREATE TABLE user (
  organization_id INT NOT NULL,
  id INT NOT NULL,
  role_id INT NOT NULL,
  name VARCHAR(80) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (role_id) REFERENCES role(id),
  FOREIGN KEY (organization_id) REFERENCES organization(id)
);

CREATE TABLE asset_type (
  organization_id INT NOT NULL,
  id INT NOT NULL,
  name VARCHAR(80) NOT NULL,
  FOREIGN KEY (organization_id) REFERENCES organization(id),
  PRIMARY KEY (id)
);

CREATE TABLE manufacturer (
  organization_id INT NOT NULL,
  id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY (organization_id) REFERENCES organization(id),
  PRIMARY KEY (id)
);

CREATE TABLE asset (
  organization_id INT NOT NULL,
  id INT NOT NULL,
  asset_type_id INT NOT NULL,
  asset_id INT,
  name VARCHAR(80),
  manufacturer_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (asset_type_id) REFERENCES asset_type(id),
  FOREIGN KEY (organization_id) REFERENCES organization(id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id)
);

CREATE TABLE assignee (
  organization_id INT NOT NULL,
  id INT NOT NULL,
  name VARCHAR(128) NOT NULL,
  FOREIGN KEY (organization_id) REFERENCES organization(id),
  PRIMARY KEY (id)
);

CREATE TABLE assignee_asset (
  assignee_id INT NOT NULL,
  asset_id INT NOT NULL,
  FOREIGN KEY (assignee_id) REFERENCES assignee(id),
  FOREIGN KEY (asset_id) REFERENCES asset(id)
);
