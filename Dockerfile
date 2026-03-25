FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia arquivos de dependência
COPY pyproject.toml poetry.lock* /app/

# Instala poetry
RUN pip install poetry

# Instala dependências do projeto
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copia o resto do projeto
COPY . /app

# Comando padrão
ENTRYPOINT ["poetry", "run", "scrapy", "crawl"]