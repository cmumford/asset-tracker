
root_dir=$(shell pwd)
app_dir = ${root_dir}/app

.PHONY: run
run:
	dev_appserver.py ${app_dir}
