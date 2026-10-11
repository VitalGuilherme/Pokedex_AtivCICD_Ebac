FROM python:3.14.6-slim

WORKDIR /app

RUN pip install poetry==1.8.3

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "pokedex:app", "--host", "0.0.0.0", "--port", "8000"]

