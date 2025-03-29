import os
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from google import genai

discord_bot_key = os.environ["DISCORD_BOT_KEY"]

bot = commands.Bot()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=GOOGLE_API_KEY)


@bot.slash_command(description="Ping command")
async def ping(interaction: Interaction):
    await interaction.response.send_message("Pong!")


@bot.slash_command(description="prompts google gemini ai")
async def gemini(
    interaction: Interaction, arg: str = SlashOption(description="Prompt")
):
    response = client.models.generate_content(model="gemini-2.0-flash", contents=arg)

    await interaction.response.send_message(response.text)


if __name__ == "__main__":
    print("starting gemini bot")
    bot.run(discord_bot_key)
