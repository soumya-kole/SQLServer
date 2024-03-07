FROM mcr.microsoft.com/mssql/server:2019-latest

WORKDIR /app

SHELL ["/usr/bin/sh", "-c"]

USER root
RUN mkdir -p /var/lib/apt/lists/partial && \
    chmod 644 /var/lib/apt/lists/partial

# Install necessary Linux libraries and tools
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    unixodbc-dev

COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
USER mssql

COPY . /app

CMD ["python3", "app.py"]
