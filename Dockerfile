FROM python:3.7.9

RUN mkdir -p /home/www/flask
WORKDIR /home/www/flask
COPY . /home/www/flask
RUN pip install -r requirements.txt

EXPOSE 9100

CMD ["python","main.py"]


