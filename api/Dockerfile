# Image Python de base
FROM python:3.12-slim

# Configuration Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Repertoire de travail
WORKDIR /code

# Installation des dependances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code de l'application
COPY app ./app

# Utilisateur non privilegie
RUN useradd --create-home --uid 10001 appuser
USER appuser

# Port de l'API
EXPOSE 8000

# Demarrage de FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
