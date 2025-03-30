FROM python:3.11

WORKDIR /usr/src/

# COPY ./api /usr/src/api
# COPY ./app.py /usr/src/app.py
COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install -r requirements.txt

RUN echo "Building..."

ENV FLASK_APP=app.py
ENV FLASK_DEBUG=TRUE

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0"]