FROM python:3.10
LABEL author='Label A'
USER root
WORKDIR /app

# Environment
RUN apt-get update
RUN apt-get install -y bash vim nano postgresql-client
RUN pip install --upgrade pip

# Major pinned python dependencies
RUN pip install --no-cache-dir flake8==3.8.4 uWSGI

# Regular Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy our codebase into the container
COPY . /app/

RUN ./manage.py collectstatic --noinput
RUN ./manage.py makemigrations sales_app

# Ops Parameters
ENV WORKERS=2
ENV PORT=80
ENV PYTHONUNBUFFERED=1

EXPOSE ${PORT}

RUN chmod +x /app/script.sh
ENTRYPOINT ["/bin/bash","-c","/app/script.sh"]
# CMD uwsgi --http :${PORT} --processes ${WORKERS} --static-map /static=/static --module autocompany.wsgi:application
