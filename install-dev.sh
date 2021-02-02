#!/bin/bash

# Virtual Environment
echo '### Setting up Virtual Environment...'
python3 -m venv venv
. venv/bin/activate

# Install Deps
echo '### Install Dependencies...'
pip install -e .

# Setup Environment
echo '### Setting Flask Environment...'
export FLASK_APP=townsquare/app.py
export FLASK_ENV=development

echo '### Final steps'
echo '1. Set environment variable for `townsquare_github_token` to your personal access token'
echo '2. $ . venv/bin/activate'
echo '3. $ flask run'
