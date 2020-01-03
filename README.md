
## Prerequisites

Python 3:
```sh
sudo apt-get install python3 python3-pip
```

### MariaDB

Install MariaDB:
```sh
sudo apt-get install mariadb-server mariadb-client
```

https://cloud.google.com/solutions/setup-mysql

Recreate the test database.

```sh
make db
```

## Setup and activate virtual environment

```sh
. ./scripts/venv_init.sh
```

## Deactivate and delete virtual environment

```sh
. ./scripts/venv_delete.sh
```

## Run the development server

```sh
make run
```

## Run tests

```sh
make test
```
