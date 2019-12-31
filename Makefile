
.PHONY: run
run:
	@[ "${VIRTUAL_ENV}" ] || ( echo ">> virtual env not active (see README.md)."; exit 1 )
	python3 app/main.py
