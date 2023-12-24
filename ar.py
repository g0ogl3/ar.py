import discord
from config import TOKEN
from bot_logic import gen_pass
from bot_logic import new_func
client = discord.Client(intents = discord.Intents.all())
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.content.channel.sent('Hello!')
    elif message.content.startswith('$bye'):
        await message.channel.send('\\U0001f642')
    else:
        await message.channel.send(message.content)
client.run(TOKEN)
gen_pass()
new_func()
