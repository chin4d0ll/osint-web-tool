# syntax=docker/dockerfile:1

# Start from a base image that includes Python.
# You can choose a specific Python version tag, e.g., python:3.9-slim-bullseye

# ใช้ base image ที่มีทั้ง Python และ Node.js
FROM mcr.microsoft.com/devcontainers/python-node:3.12-bullseye


## Node.js และ npm ติดตั้งมาแล้วใน base image ไม่ต้องติดตั้งซ้ำ

# [Optional] Install Chrome and ChromeDriver for Selenium
# This section can be expanded if you need specific versions or configurations
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    # Install Chrome
    wget \
    gnupg \
    ca-certificates \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    # Install ChromeDriver (adjust version as needed or download specific version)
    # For simplicity, this example installs a version that's often compatible.
    # You might need to manage ChromeDriver versions more carefully for production.
    && CHROME_DRIVER_VERSION=$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(google-chrome --version | cut -d ' ' -f 3 | cut -d '.' -f 1,2,3)) \
    && wget -qO /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip" \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip \
    && chmod +x /usr/local/bin/chromedriver \
    # Clean up
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# [Optional] Set the working directory in the container
WORKDIR /workspaces/osint-web-tool

# [Optional] Copy application dependency manifests to the container image.
# This is often done to leverage Docker cache layers.
COPY backend/requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

COPY frontend/package.json frontend/package-lock.json* /tmp/npm-tmp/
# If you use yarn, you would also copy yarn.lock: frontend/yarn.lock*
RUN cd /tmp/npm-tmp && npm install --omit=dev && npm cache clean --force \
   && rm -rf /tmp/npm-tmp

# [Optional] Expose ports (if your application listens on them)
# EXPOSE 5001 3000

# [Optional] Default command.
# CMD [ "sleep", "infinity" ]
