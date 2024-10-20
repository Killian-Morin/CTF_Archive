FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y git build-essential python3-dev

RUN pip install volatility3

# Install Volatility
WORKDIR /volatility
# RUN python3 setup.py install
