# Selenium UI automation using Python.
UI automation using python &amp; selenium.

## Installation

Install pythng 3.7 and setup the env using pyenv
- `python3.7 -m venv ./env
- `source env/bin/activate`
Install selenium using pip
- `pip install selenium`
Install Drivers for chrome, firefox & safari. I am using chrome for this project.
- https://sites.google.com/a/chromium.org/chromedriver/downloads

## Available Automation Commands
Check the env-sample file and update the env file depending on the chrome version. The driver version is different for chrome and the docker uses driver version 78.
- `python specs/python_org_search.py` - run tests in command-line and browser. To run headless check specs/python_org_search.py file line 10.
Run tests on docker.
- `docker-compose up`

## Note
Ref. https://selenium-python.readthedocs.io/
