FROM python:3.11-buster

WORKDIR /root

RUN apt-get update && apt-get install -y curl

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

RUN poetry config virtualenvs.in-project true

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY ./src ./src

CMD ["tail", "-f", "/dev/null"]