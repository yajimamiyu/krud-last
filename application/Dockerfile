FROM python:3.11.9

RUN mkdir /code/
COPY ./ /code/
WORKDIR /code/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv --python /usr/local/bin/python
RUN pipenv install

CMD pipenv run python manage.py runserver 0:8000
