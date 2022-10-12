FROM ubuntu:22.04

COPY runner.sh /etc/cron.hourly/

RUN apt-get update && \
    apt-get -y dist-upgrade && \
    apt-get -y install \
        python3 \
        python3-venv \
        python3-pip \
        cron \
        wget \
        unzip \
        fonts-liberation \
        libasound2 \
        libatk-bridge2.0-0 \
        libatk1.0-0 \
        libatspi2.0-0 \
        libcairo2 \
        libcups2 \
        libcurl3-gnutls \
        libcurl3-nss \
        libcurl4 \
        libdbus-1-3 \
        libdrm2 \
        libgbm1 \
        libglib2.0-0 \
        libgtk-3-0 \
        libgtk-4-1 \
        libnspr4 \
        libnss3 \
        libpango-1.0-0 \
        libwayland-client0 \
        libx11-6 \
        libxcb1 \
        libxcomposite1 \
        libxdamage1 \
        libxext6 \
        libxfixes3 \
        libxkbcommon0 \
        libxrandr2 \
        xdg-utils && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb && \
    wget https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/local/bin && \
    python3 -m ensurepip --upgrade && \
    pip install selenium && \
    pip install undetected_chromedriver && \
    pip install requests

ENTRYPOINT [ "/bin/sh" ]