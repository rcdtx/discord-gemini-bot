import os

import google.generativeai as genai

import discord
from discord.ext import commands

discord_bot_key = os.environ["DISCORD_BOT_KEY"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=">", intents=intents)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!gemini"):
        response = model.generate_content(message.content[8:])
        try:
            await message.channel.send(response.text)
        except discord.errors.HTTPException:
            await message.channel.send(response.text)


if __name__ == "__main__":
    try:
        bot.run(discord_bot_key)
    except:
        os.system("kill 1")
