FROM tiangolo/uwsgi-nginx-flask:python3.9

WORKDIR /app

#RUN pip install poetry
#
#RUN poetry config virtualenvs.create false
#
#COPY ./pyproject.toml .
#COPY ./poetry.lock .
RUN pip install -U pip
RUN pip install setuptools wheel

COPY requirements.txt ./
RUN pip install -r requirements.txt


#RUN poetry install

COPY ./ ./
