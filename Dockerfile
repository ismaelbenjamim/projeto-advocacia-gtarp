FROM python:3.9-slim-buster

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONPATH=/code/ \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  DEBUG=False \
  ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0
  SECRET_KEY='AquiVemSuaMegaSuperChaveSecreta'
  # Averiguar modo seguro de se passar a secret key!
  # DATABASE_URL deve ser definida no caso de ser usado o Postgres, do contrário será usado o SQLite como banco default.

# Define work directory
WORKDIR /code/

# Install project dependencies
RUN pip install -U pip &&\
    pip install --no-color \
    --no-cache-dir \
    --disable-pip-version-check \
    --retries 1 \
    "Django==3.2" \
    "python-decouple==3.4" \
    "dj-database-url==0.5.0" \
    "psycopg2-binary==2.8.6" \
    "gunicorn==20.1.0"

COPY projeto_advocacia /code/

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "projeto_advocacia:application"]