# Meet.ai

## English

Meet.ai is a meeting bot that connects to Google Meet, records audio, transcribes speech, and provides meeting summaries. It uses SeleniumBase for browser automation, PyAudio for audio recording, and Google Cloud Speech-to-Text API for speech recognition. It uses `meet_bot.py`, `speech_rec.py`, `summarizer.py`, `audio_recorder.py` and `config.py` files.

### Features

*   Connects to Google Meet using SeleniumBase
*   Records audio using PyAudio
*   Transcribes speech to text using Google Cloud Speech-to-Text API
*   Provides meeting summaries (future implementation)
*   Containerized using Docker for easy deployment

### Requirements

*   Python 3.6+
*   SeleniumBase
*   PyAudio
*   SpeechRecognition
*   Google Cloud Speech-to-Text API key
*   Google Meet account
*   OpenAI API key
*   Docker (for containerized deployment)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/your-username/meet.ai.git
    cd meet.ai
    ```
2.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```
3.  Set up Google Cloud Speech-to-Text API:

    *   Create a Google Cloud project.
    *   Enable the Speech-to-Text API.
    *   Create a service account and download the credentials file.
    *   Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of the credentials file.

4.  Run the bot:

    ```bash
    python app.py --meet-url <meet_url> --user-name <user_name> --output-file-name <output_file_name> --language <language> --api-key <api_key>
    ```

    *   `--meet-url`: Google Meet URL (required).
    *   `--user-name`: User name for Google Meet (optional, default: "Ai Bot").
    *   `--output-file-name`: Output file name for audio recording (optional, default: "output.wav").
    *   `--language`: Language for speech recognition (optional, default: "tr-TR").
    *   `--api-key`: OpenAI API key (required).

### Docker Deployment

1.  Build the Docker image:

    ```bash
    docker build -t meet.ai .
    ```
2.  Run the Docker container:

    ```bash
    docker-compose up
    ```

## Türkçe

Meet.ai, Google Meet'e bağlanan, ses kaydeden, konuşmayı yazıya döken ve toplantı özetleri sağlayan bir toplantı botudur. Tarayıcı otomasyonu için SeleniumBase, ses kaydı için PyAudio ve konuşma tanıma için Google Cloud Speech-to-Text API'sini kullanır. It uses `meet_bot.py`, `speech_rec.py`, `summarizer.py`, `audio_recorder.py` and `config.py` files.

### Özellikler

*   SeleniumBase kullanarak Google Meet'e bağlanır
*   PyAudio kullanarak ses kaydeder
*   Google Cloud Speech-to-Text API'sini kullanarak konuşmayı metne dönüştürür
*   Toplantı özetleri sağlar (gelecekteki uygulama)
*   Kolay dağıtım için Docker kullanılarak konteynerize edilmiştir

### Gereksinimler

*   Python 3.6+
*   SeleniumBase
*   PyAudio
*   SpeechRecognition
*   Google Cloud Speech-to-Text API anahtarı
*   Google Meet hesabı
*   OpenAI API anahtarı
*   Docker (konteynerize edilmiş dağıtım için)

### Kurulum

1.  Depoyu klonlayın:

    ```bash
    git clone https://github.com/your-username/meet.ai.git
    cd meet.ai
    ```
2.  Bağımlılıkları yükleyin:

    ```bash
    pip install -r requirements.txt
    ```
3.  Google Cloud Speech-to-Text API'sini ayarlayın:

    *   Bir Google Cloud projesi oluşturun.
    *   Speech-to-Text API'sini etkinleştirin.
    *   Bir hizmet hesabı oluşturun ve kimlik bilgileri dosyasını indirin.
    *   `GOOGLE_APPLICATION_CREDENTIALS` ortam değişkenini, kimlik bilgileri dosyasının yoluna ayarlayın.

4.  Botu çalıştırmak için:

    ```bash
    python app.py --meet-url <meet_url> --user-name <user_name> --output-file-name <output_file_name> --language <language> --api-key <api_key>
    ```

    *   `--meet-url`: Google Meet URL'si (gerekli).
    *   `--user-name`: Google Meet için kullanıcı adı (isteğe bağlı, varsayılan: "Ai Bot").
    *   `--output-file-name`: Ses kaydı için çıktı dosya adı (isteğe bağlı, varsayılan: "output.wav").
    *   `--language`: Konuşma tanıma için dil (isteğe bağlı, varsayılan: "tr-TR").
    *   `--api-key`: OpenAI API anahtarı (gerekli).

### Docker ile Dağıtım

1.  Docker görüntüsünü oluşturun:

    ```bash
    docker build -t meet.ai .
    ```
2.  Docker konteynerini çalıştırın:

    ```bash
    docker-compose up
