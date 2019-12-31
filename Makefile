
root_dir=$(shell pwd)
app_dir = ${root_dir}/goapp

.PHONY: run
run:
	dev_appserver.py ${app_dir}
