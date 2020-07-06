import discord, json
from discord.ext import commands
error_icon = 'https://cdn.discordapp.com/emojis/678014140203401246.png?v=1'
Client = discord.Client()
TOKEN = open('/root/Support/token.txt', 'r').read()
# TOKEN = open('/Users/duckmasteral/Documents/GitHub/quacky-support/token.txt').read()

initial_extensions = ['admin', 'moderation', 'misc', 'ticket', 'events']

async def get_prefix(bot, message):
  return ['!', '<@!721865235413205014}> ', '<@721865235413205014> ', '<@721865235413205014>', '<@!721865235413205014>']

client = commands.Bot(command_prefix=get_prefix, case_insensitive=True)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Quacky Support: {extension} could not be loaded!\n{type(e).__name__}: {e}')

client.run(TOKEN)