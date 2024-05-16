FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

# Install any needed packages specified in pyproject.toml
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

EXPOSE 8000

# Run app.py when the container launches
CMD ["uvicorn", "sqlagent.app:app", "--host", "0.0.0.0", "--port", "8000"]