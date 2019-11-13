# Selenium UI automation using Python.
UI automation using python &amp; selenium. The sample tests are run on chrome and firefox.
The docker image used supports chrome version 78.0 and Mozilla firefox version 65.0. The docker image repository [docker-selenium-python](https://github.com/deepakhb2/docker-selenium-python)

## Installation

Install pythng 3.7 and setup the env using pyenv
- `python3.7 -m venv ./env`
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

## Azure CI run badge
[![Build Status](https://dev.azure.com/deepakhb20379/deepakhb2/_apis/build/status/deepakhb2.python-ui-automation?branchName=master)](https://dev.azure.com/deepakhb20379/deepakhb2/_build/latest?definitionId=4&branchName=master)

## Note
Ref. https://selenium-python.readthedocs.io/
