# Use an ARM64 base image
FROM kalilinux/kali-rolling:latest

WORKDIR /usr/src/app/

# common CTF tools
RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    autoconf \
    automake \
    git \
    libtool \
    ncurses-dev \
    libgmp-dev \
    python3 \
    python3-pip \
    nmap \
    metasploit-framework \
    hashcat \
    gdb \
    binwalk \
    file \
    wget \
    curl \
    && apt-get clean

# Expose port for web challenges
# EXPOSE 80
