FROM python:3.9-bullseye

WORKDIR /usr/src/app

RUN pip install --upgrade pip

RUN pip install python-dotenv

RUN pip install --no-cache-dir \
    pwntools
    # ipython

# Copy '.' into the container at /usr/src/app
COPY 796b04f8d15181b2c5885b7df6a754197866210f.jpeg .

# Add a command to keep the container running. This can be a simple command like tail -f /dev/null
CMD ["tail", "-f", "/dev/null"]