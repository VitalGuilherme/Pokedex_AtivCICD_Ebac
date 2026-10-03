FROM python:3.14.6

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . .

CMD ["poetry", "run", "uvicorn", "pokedex.py"]

