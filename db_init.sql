CREATE USER 'asset-web'@'localhost' IDENTIFIED BY 'password';

CREATE DATABASE easy_asset_tracker;

GRANT ALL PRIVILEGES ON * . * TO 'asset-web'@'localhost';
FLUSH PRIVILEGES;
