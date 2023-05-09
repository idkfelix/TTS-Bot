from sys import argv
from requests import post
from os import remove, path
from uuid import uuid4
from discord import Intents,File
from discord.ext import commands
from yaml import safe_load as yaml_load

if not path.exists("config.yaml"):
    dconfig = "discord_bot_token: \neleven_key: \neleven_voiceID: \nbot_name: "
    with open("config.yaml", "w") as f:
                f.write(dconfig)
    exit("Fill out the config.yaml file")
else:
    with open("config.yaml", 'r') as f:
            config = yaml_load(f)


intents = Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    if path.exists("pfp.png"):
        with open('pfp.png', 'rb') as image:
            await client.user.edit(avatar=image.read(), username=config.bot_name)
    else:
         await client.user.edit(username=config.bot_name)
    print(f'{client.user} has connected to Discord!')

@client.command()
async def tts(ctx, text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{config['eleven_voiceID']}"
    headers = {
        'xi-api-key': config["eleven_key"],
        'accept': 'audio/mpeg'
    }
    body = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
        "stability": 0.25,
        "similarity_boost": 0.25
        }
    }
    r = post(url, headers=headers, json=body)
    filename = str(uuid4()) + '.mp3'
    with open(filename, 'wb') as f:
        f.write(r.content)
    await ctx.send(file=File(filename))
    remove(filename)

try:
    client.run(config["discord_bot_token"])
except AttributeError:
    exit("Check your config.yaml file")