FROM python:3.9.7

COPY TTS-Bot.py ./
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "TTS-Bot.py"]