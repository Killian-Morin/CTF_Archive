FROM python:3.9-bullseye

WORKDIR /usr/src/app

RUN pip install --upgrade pip

RUN pip install python-dotenv

# RUN pip install --no-cache-dir \
    # viz-image-deobfuscate
    # ipython

# Copy '.' into the container at /usr/src/app
COPY script.py .

# Add a command to keep the container running. This can be a simple command like tail -f /dev/null
CMD ["tail", "-f", "/dev/null"]