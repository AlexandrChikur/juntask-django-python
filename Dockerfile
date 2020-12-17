FROM python:3.8-slim

ENV  \
    #python
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    #poetry
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VERSION=1.1.4

RUN apt-get update \
    && python -m pip install --upgrade pip \
    && pip install "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.in-project true

WORKDIR /task
COPY ./scripts /scripts
COPY ./poetry.lock ./pyproject.toml /task/

RUN poetry install --no-dev

RUN chmod +x /scripts/*

ENTRYPOINT ["/scripts/entrypoint.sh"]

COPY . /task
