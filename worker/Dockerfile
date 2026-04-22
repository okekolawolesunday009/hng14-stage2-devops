FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Test stage — adds pytest on top of base, never ships
FROM base AS test
RUN pip install --no-cache-dir pytest pytest-coverage
COPY . .

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD wget --no-verbose --tries=1 --spider http://localhost:6379/ || exit 1
CMD ["python", "worker.py"]