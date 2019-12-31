
## Prerequisites

Python 3:
```sh
sudo apt-get install python3 python3-pip
```

### MySQL

Install MySQL:
```sh
sudo apt-get install mysql-server mysql-client
```

https://cloud.google.com/solutions/setup-mysql

```sql
CREATE USER 'asset-web'@'localhost' IDENTIFIED BY 'password';
CREATE DATABASE easy-asset-tracker;
GRANT ALL PRIVILEGES ON * . * TO 'asset-web'@'localhost';
FLUSH PRIVILEGES;
```

## Setup and activate virtual environment

```sh
. ./venv_init.sh
```

## Deactivate and delete virtual environment

```sh
. ./venv_delete.sh
```

## Run the development server

```sh
make run
```

## Run tests

```sh
make test
```
