FROM python:3.9.7

COPY ./* ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "TTS-Bot.py"]