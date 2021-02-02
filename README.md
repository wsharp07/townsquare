## Townsquare

### Install

Create a virtualenv and activate it:

    $ python3 -m venv venv
    $ . venv/bin/activate

Or on Windows cmd:

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat

Install Townsquare:

    $ pip install -e .

Or if you are using the master branch, install Flask from source before
installing Townsquare:

    $ pip install -e ../..
    $ pip install -e .

Install dependencies:

    $ pip install -r requirements.txt

### Configure Environment
Set an environment variable with your GitHub Personal Access token

    townsquare_github_token="personal access token"

### Run

    $ export FLASK_APP=townsquare/app.py
    $ export FLASK_ENV=development
    $ flask run

Or on Windows cmd

    > set FLASK_APP=townsquare
    > set FLASK_ENV=development
    > flask run

Open http://127.0.0.1:5000 in a browser

### Test

    $ pytest

Run with coverage report::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser