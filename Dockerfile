# x86_64 mimarisini zorla (ARM'de emülasyonla çalışır)
FROM --platform=linux/amd64 python:3.11-slim

# Chrome kullanıcısını oluştur (root olarak)
RUN useradd -m -G audio,video chromeuser && \
    mkdir -p /home/chromeuser/Downloads && \
    chown -R chromeuser:chromeuser /home/chromeuser

# Çalışma dizinini ayarla ve sahipliği düzenle
WORKDIR /app
RUN chown -R chromeuser:chromeuser /app

# Root olarak bağımlılıkları kur
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    gnupg \
    unzip \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcairo2 \
    libcups2 \
    libcurl4 \
    libdbus-1-3 \
    libexpat1 \
    libgbm1 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libudev1 \
    libvulkan1 \
    libx11-6 \
    libxcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    python3-pyaudio \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Google Chrome'u indir ve kur
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get update && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    rm -rf /var/lib/apt/lists/*

# Chromedriver'ı manuel olarak indir ve kur
RUN wget -q https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.90/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip -d /usr/local/bin/ && \
    mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf chromedriver-linux64.zip /usr/local/bin/chromedriver-linux64

# Uygulama dosyalarını kopyala ve bağımlılıkları kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# İndirilen dosyalar için klasör oluştur

# After installing requirements but before switching to chromeuser
RUN mkdir -p /usr/local/lib/python3.11/site-packages/seleniumbase/drivers/ && \
    chmod -R 777 /usr/local/lib/python3.11/site-packages/seleniumbase/drivers/

RUN mkdir -p /app/downloaded_files && \
    chown -R chromeuser:chromeuser /app/downloaded_files \
    && chown -R chromeuser:chromeuser /app

# Chrome kullanıcısına geç
USER chromeuser

# Varsayılan komut (XVFB ile headless modda çalıştır)
CMD ["python", "app.py"]
