import responses
import discord 
from discord.ext import commands
from discord.ext.commands import Bot

TOKEN = 'MTA4MzQ5NTgwNzQ0MzAxMzc2OA.GlIn9-.Imt4KPrn6WeqiR0OJFFs6mmzoumLoJ1WVCWT0E'
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)
#client = commands.Bot(command_prefix="!")

# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

@client.event
async def on_ready():
    print(f'{client.user} is now running!')


@client.event
async def on_message(message):
    # Make sure bot doesn't get stuck in an infinite loop
    if message.author == client.user:
        return

    # Get data about the user
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    # Debug printing in vs code console
    print(f"{username} said: '{user_message}' ({channel})")

    if user_message[0] == '?':
        user_message = user_message[1:]  # [1:] Removes the '?'
        await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)

    



client.run(TOKEN)
#if __name__ == '__main__':
#    bot.run_discord_bot()