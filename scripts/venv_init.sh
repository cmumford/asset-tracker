#!/bin/bash -xe

venv_dir=venv

if [[ ! -d "${venv_dir}" ]]; then
  echo "Creating Python virtual environment."
  python3 -m venv ${venv_dir}
fi

if [[ -z "${VIRTUAL_ENV}" ]]; then
  echo "Activating Python virtual environment."
  source ${venv_dir}/bin/activate
fi

# Don't want to install to production server.
echo "Instlling Python developer prerequesites..."
pip3 install -r dev_requirements.txt

echo "Instlling Python prerequesites..."
pip3 install -r app/requirements.txt
