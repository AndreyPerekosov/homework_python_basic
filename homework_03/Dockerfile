FROM python:3.9-buster

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY ./web-app/pyproject.toml .
COPY ./web-app/poetry.lock .

RUN poetry install

COPY web-app ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]

# запуск контейнера на порту 8000: docker run -p 8000:8000 web-app