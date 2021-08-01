import discord
from discord.ext import commands
import traceback
import sys

bot = commands.Bot(command_prefix=".")

bot.remove_command("help")

DISCORD_TOKEN = 'ODY3MDA1MjU5ODcyMjA2ODk5.YPazkg.dGRmt6RaFyEPOyVkJnWmWBdlSZY'

initial_extensions = ['cogs.voice']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(DISCORD_TOKEN)
