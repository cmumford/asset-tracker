
root_dir=$(shell pwd)
app_dir = app

.PHONY: run
run:
	dev_appserver.py ${app_dir}

.PHONY: clean
clean:
	echo "Did you deactivate?"
	rm -rf venv
