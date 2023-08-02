import disnake
from disnake.ext import commands
import io
import requests

data = {i.split('=')[0]: '='.join(i.split('=')[1::]) for i in open("config.txt", 'r').read().splitlines() if i}

client = commands.Bot(command_prefix='sorter ', intents=disnake.Intents().all())

@client.event
async def on_ready():
    print(f"{client.user} is ready to sort!")
    await client.change_presence(status=disnake.Status.idle, activity=disnake.Activity(type=disnake.ActivityType.playing, name="Sorting", url="https://github.com/NacreousDawn596"))

@client.event
async def on_message(msg):
    if msg.startswith("sorter run "): return await msg.reply(exec('\n'.join(msg.splitlines()[1::])))

    if msg.author == client.user or not any([i in msg.channel.name for i in data['the upload channel gonna contain some of these strings'].split(', ')]): return
    
    channels = sorted([channel for channel in msg.guild.channels if str(channel.type) == 'text' and data['saves gonna have'] in channel.name])

    if not channels: 
        channels = [await msg.guild.create_text_channel(data['saves gonna have'] + '-0')]

    channel, i = channels[-1], int(channels[-1].name.split('-')[-1])

    datas = await channel.history(limit=100).flatten()

    for pic in [attch.url for attch in msg.attachments]:
        if len(datas) <= 100:
            try:
                await channel.send(file=disnake.File(io.BytesIO(requests.get(pic).content), pic.split('/')[-1]))
            except:
                await msg.reply('oops! something went wrong with: ' + pic)
        else:
            channel = await msg.guild.create_text_channel(data['saves gonna have'] + '-' + i)
            i += 1

    for url in [urls for urls in msg.content if 'http' in urls]:
        if len(datas) <= 100:
            try:
                await channel.send(file=disnake.File(io.BytesIO(requests.get(url).content), url.split('/')[-1]))
            except:
                await msg.reply('oops! something went wrong with: ' + url)
        else:
            channel = await msg.guild.create_text_channel(data['saves gonna have'] + '-' + i)
            i += 1
    
    return await msg.reply('done, saved!')

client.run(data['token'])

