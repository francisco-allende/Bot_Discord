import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as dt
import responses

# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA4MzQ5NTgwNzQ0MzAxMzc2OA.GlIn9-.Imt4KPrn6WeqiR0OJFFs6mmzoumLoJ1WVCWT0E'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)
    bot = commands.Bot(command_prefix='!', intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @bot.command()
    async def hello(ctx):
        await ctx.send("hola soy un bot")

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

        # Direct Message. If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Removes the '?'
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @bot.command(pass_context=True)
    async def test(ctx):
         await ctx.send(file=discord.File(r'c:\location\of\the_file_to\send.png'))

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)