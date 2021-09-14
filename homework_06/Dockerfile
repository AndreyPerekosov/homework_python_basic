FROM tiangolo/uwsgi-nginx-flask:python3.9

WORKDIR /app

RUN pip install poetry
#
RUN poetry config virtualenvs.create false
#
COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN poetry install

COPY ./ ./
