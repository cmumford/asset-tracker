
USE easy_asset_tracker;

CREATE TABLE role (
  id INT NOT NULL,
  name VARCHAR(80),
  PRIMARY KEY (id)
);

CREATE TABLE user (
  id INT NOT NULL,
  role_id INT NOT NULL,
  name VARCHAR(80),
  PRIMARY KEY (id),
  FOREIGN KEY (role_id) REFERENCES role(id)
);

CREATE TABLE asset_type (
  id INT NOT NULL,
  name VARCHAR(80),
  PRIMARY KEY (id)
);

CREATE TABLE manufacturer (
  id INT NOT NULL,
  name VARCHAR(256),
  PRIMARY KEY (id)
);

CREATE TABLE asset (
  id INT NOT NULL,
  asset_type_id INT NOT NULL,
  asset_id INT,
  name VARCHAR(80),
  manufacturer_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (asset_type_id) REFERENCES asset_type(id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id)
);
