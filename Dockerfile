FROM deepakhb2/selenium-python-browsers:latest 

WORKDIR /code
ADD . /code

RUN pip install -r requirements.txt
