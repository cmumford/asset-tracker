#!/bin/bash -xe

venv_dir=venv

if [[ ! -z "${VIRTUAL_ENV}" ]]; then
  echo "Deactivating Python virtual environment."
  deactivate
fi

if [[ -d "${venv_dir}" ]]; then
  echo "Deleting Python virtual environment."
  rm -r ${venv_dir}
fi
