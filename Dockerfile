FROM apache/airflow:2.10.2

USER root

# Install Google Chrome and dependencies
RUN apt-get update && apt-get install -y wget gnupg2 \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update && apt-get install -y google-chrome-stable \
    && apt-get install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 libxrender1 libx11-6 libxcomposite1 libxext6 libxi6 libxdamage1 libxtst6 libxrandr2 libasound2 libatk1.0-0 libgtk-3-0


USER airflow

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt