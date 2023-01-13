from discord.ext import commands
from discord import Embed
import platform
import discord


class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command(aliases=['bot info'])
    async def info(self, ctx):
        embed = Embed(title=f'{self.bot.user.name} Bot \n',
                      colour=0x921030)

        py_version = platform.python_version()
        discord_py = discord.__version__
        numbers_of_server = len(self.bot.guilds)
        numbers_of_members = len(set(self.bot.get_all_members()))
        embed.add_field(name='Developers and Source Code',
                        value=f':page_facing_up: Source code on [github](https://github.com/0x73hahd/0x73hahd-bot)\n'
                              f':star: [Developer account](https://github.com/0x73hahd)\n', inline=True)
        embed.add_field(name=':green_circle: **Guilds:** ', value=f'\t **{numbers_of_server}\n**', inline=True)
        embed.add_field(name=':busts_in_silhouette: **Members:**  ', value=f'\t **{numbers_of_members}\n**')
        embed.add_field(name='About Bot',
                        value=f'\nThis bot written in python version {py_version} '
                              f'with discord.py library version {discord_py}' + '\n' * 3,
                        inline=True)
        embed.set_thumbnail(url='https://avatars.githubusercontent.com/u/100186933?s=400&u=5781c8e508b79d8a22b1032fd1b05f0c5c602097&v=4')
        embed.set_footer(text='Developed by 0x73hahd#0030')
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(BotInfo(bot))

