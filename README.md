# to get all the uploaded and saved files:

```py
import disnake
from disnake.ext import commands

client = commands.Bot(command_prefix=data['prefix'], intents=disnake.Intents().all())

@client.event
async def on_ready():
    print(f"{client.user} is currently collecting...")
    guild = client.guilds[int(input('\n'.join(f"{i}) {j.name}" for i, j in enumerate(client.guilds)) + '\n=> '))]
    uploades = sum([await channel.history(limit=100).flatten() for channel in msg.guild.channels if str(channel.type) == 'text' and data['saves gonna have'] in channel.name], [])
    """
        do something with the uploades list, it's a list that contains all the urls of the uploads
        ...
        ...
        ...
        ...
    """
```

**enjoy!**
