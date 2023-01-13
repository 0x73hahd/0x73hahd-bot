import os
import logging
import discord
from pathlib import Path
from discord import Game
from discord.ext import commands
from configs import Configs

# Get current working directory
cwd = Path(__file__).cwd()
cwd = str(cwd)
print(f'{cwd}\n' + '~' * len(cwd))

configs = Configs.instance()

intents = discord.Intents.default()
intents.message_content = True
handler = logging.FileHandler(filename='discord.log',
                              encoding='utf-8', mode='w')


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='$',
                         intents=intents,
                         strip_after_prefix=True,
                         description='',
                         activity=Game(name=''))

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        await self.load_extension('jishaku')
        try:
            for file in os.listdir(cwd + '/cogs'):
                if file.endswith('.py'):
                    print(f'cogs.{file}')
                    await self.load_extension(f'cogs.{file[:-3]}')
        except Exception as exception:
            print(f'Failed while loading the extension\n{exception}')


Bot().run(configs.discord_token)
