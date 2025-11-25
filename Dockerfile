FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN sed -i 's/\r$//' entrypoint.sh && \
    chmod +x entrypoint.sh && \
    adduser --disabled-password --gecos "" appuser && \
    chown -R appuser /app

USER appuser

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=demo.settings

HEALTHCHECK --interval=30s --timeout=10s --start-period=20s \
  CMD curl -f http://localhost:8000/health/ || exit 1

CMD ["./entrypoint.sh"]
