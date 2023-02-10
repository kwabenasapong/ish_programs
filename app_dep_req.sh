#!/usr/bin/env bash
# dependencies for gunicorn

sudo apt update
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools -y
sudo apt install python3-venv -y
mkdir ~/myproject_guicorn
cd ~/myproject_gunicorn || exit
python3 -m venv myprojectenv
source myprojectenv/bin/activate
pip install wheel
pip install gunicorn flask
