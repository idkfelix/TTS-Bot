<div align="center">

  <h2>TTS Bot</h1>
  <h3>A Dockerised Python TTS Discord Bot Using Elevenlabs AI</h3>

  <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Badge">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python Badge">
  <img src="https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white" alt="Discord Badge">

</div>

## Description

This is a Python Discord TTS (text-to-speech) bot that uses the ElevenLabs AI API to generate high-quality speech from text messages sent in a Discord server. The bot is containerized using Docker for easy deployment and management.

## Features

- Speech synthesis of text messages in real-time using ElevenLabs AI API
- Automatic language detection based on message content
- Dockerized for easy deployment and management

## Requirements

- Python 3.6+
- Docker

## Docker Setup

1. Clone this repository to your local machine
3. Create a `config.yaml` file in the root directory of the project, containing the following information:

```
discord_bot_token: <yourToken>
eleven_key: <yourKey>
eleven_voiceID: <yourVoiceID>
```
Replace `<yourToken>` with your Discord bot token, `<yourKey>` with your ElevenLabs API key and `<yourVoiceID>` with your selected voice model ID which can be found using the [Elevenlabs API](https://api.elevenlabs.io/docs#/voices/Get_voices_v1_voices_get).
   
3. Build the Docker image using the following command:
  
   ```
   docker build -t tts-bot .
   ```

4. Run the Docker container and mount your config file using the following command:

   ```
   docker run -d discord-tts-bot -v </path/to/config.yaml>:/config.yaml
   ```
   Replace `</path/to/config.yaml>` with the path to your local config.yaml file.

## Local Setup

1. Clone this repository to your local machine
2. Create a `config.yaml` file in the root directory of the project, containing the following information:

```
discord_bot_token: <yourToken>
eleven_key: <yourKey>
eleven_voiceID: <yourVoiceID>
```
Replace `<yourToken>` with your Discord bot token, `<yourKey>` with your ElevenLabs API key and `<yourVoiceID>` with your selected voice model ID which can be found using the [Elevenlabs API](https://api.elevenlabs.io/docs#/voices/Get_voices_v1_voices_get).

3. Install the requirements.txt with pypi using the following command:

```
pip install --no-cache-dir -r requirements.txt
```

4. run the TTS-Bot.py file with python using the following command:

```
python TTS-Bot.py
```

## Usage

Once the bot is up and running in your Discord server, simply type a message in any channel and the bot will respond with the text-to-speech version of your message.

You can also use the `!tts` command to force the bot to read a specific message, like this:

```
!tts "<your message here>"
```
