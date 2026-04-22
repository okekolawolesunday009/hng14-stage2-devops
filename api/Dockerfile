FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Test stage — adds pytest on top of base, never ships
FROM base AS test
RUN pip install --no-cache-dir pytest pytest-coverage
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]