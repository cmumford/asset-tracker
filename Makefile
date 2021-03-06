PORT=8080
PROJECT_ID=easy-asset-tracker
ENV_ERR=">> ERROR: virtual env not active (see README.md)."

# When running the development server.
export CLOUD_SQL_USERNAME=asset-web
export CLOUD_SQL_PASSWORD=password
export CLOUD_SQL_DATABASE_NAME=easy_asset_tracker

.PHONY: run
run:
	@[ "${VIRTUAL_ENV}" ] || ( echo ${ENV_ERR}; exit 1 )
	python3 main.py

# Doesn't work well for Python3 apps. Some GAE docs suggest using it
# and others suggest `run` above.
.PHONY: devserver
devserver:
	cd app && dev_appserver.py --application=${PROJECT_ID} app.yaml

# So far untested.
.PHONY: unicorn
unicorn:
	@[ "${VIRTUAL_ENV}" ] || ( echo ${ENV_ERR}; exit 1 )
	cd app && gunicorn -b :${PORT} main:app

.PHONY: unit_tests
unit_tests:
	@[ "${VIRTUAL_ENV}" ] || ( echo ${ENV_ERR}; exit 1 )
	pytest --setup-show app/tests/unit/

.PHONY: functional_tests
functional_tests:
	@[ "${VIRTUAL_ENV}" ] || ( echo ${ENV_ERR}; exit 1 )
	pytest --setup-show app/tests/functional/

.PHONY: test
test: unit_tests functional_tests

.PHONY: db
db:
	scripts/db_delete.sh
	scripts/db_init.sh
	scripts/create_schema.sh
