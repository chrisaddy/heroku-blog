FROM ubuntu
FROM python

WORKDIR /app
ADD . /app

### pip installs
RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "app.py"]