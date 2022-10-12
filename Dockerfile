FROM ubuntu:22.04

ENV xu_BASERATE=0.5
ENV xu_FILEPATH=""
ENV xu_CONFIGPATH="/config/default"
ENV xu_USERNAME=""
ENV xu_PASSWORD=""
ENV st_APIKEY=""
ENV st_SERVER="127.0.0.1"
ENV st_PORT="8384"
ENV xu_MAXSEND=0
ENV xu_MAXRECV=0
ENV xu_INTOTAL=0
ENV xu_OUTTOTAL=0

COPY runner.sh /config/

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
    pip install selenium && \
    pip install undetected_chromedriver && \
    pip install requests

ENTRYPOINT [ "/config/runner.sh" ]