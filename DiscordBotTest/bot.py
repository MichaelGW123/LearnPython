import random
import asyncpraw
import discord
import sys
import asyncio
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
try:
    TOKEN = os.getenv('DISCORD_TOKEN')
    ID = os.getenv('CLIENT_ID')
    SECRET = os.getenv('CLIENT_SECRET')
    AGENT = os.getenv('USER_AGENT')
except KeyError as e:
    print("Variables not correctly set.")


if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

reddit = asyncpraw.Reddit(client_id = ID, client_secret = SECRET, user_agent = AGENT)

client = discord.Client()

bot_prefix = '$'
cmd_one_HT = 'hello there'
cmd_two_shrimp = 'shrimp'

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

async def shrimp(message):
    sub = await reddit.subreddit('shrimptank')
    posts = []
    count = 0
    LIMIT = 50
    async for submission in sub.hot(limit=LIMIT):
        url = str(submission.url)

        if (url.endswith('jpg') or url.endswith('jpeg') or url.endswith('png')):
            posts.append(url)

            if count == LIMIT:
                break

    response = random.choice(posts)

    sub = None
    try:
        await message.channel.send(response)
    except:
        print("Error sending message")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if (message.author == client.user) or not (message.content.startswith(bot_prefix)): return

    if (message.content.startswith(bot_prefix+cmd_one_HT)):
        await message.channel.send('General Kenobi...')

    if (message.content.startswith(bot_prefix+cmd_two_shrimp)):
        quote = get_quote()
        await shrimp(message)
        await message.channel.send(quote)
    elif (message.content.startswith(bot_prefix+'basic'+cmd_two_shrimp)):
        await shrimp(message)


client.run(TOKEN)