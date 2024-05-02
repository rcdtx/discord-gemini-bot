import os

from nextcord import Interaction, SlashOption
from nextcord.ext import commands
import google.generativeai as genai
from google.generativeai.types import HarmBlockThreshold, HarmCategory


discord_bot_key = os.environ["DISCORD_BOT_KEY"]

bot = commands.Bot()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")


@bot.slash_command(description="Ping command")
async def ping(interaction: Interaction):
    await interaction.response.send_message("Pong!")


@bot.slash_command(description="prompts google gemini ai")
async def gemini(
    interaction: Interaction, arg: str = SlashOption(description="Prompt")
):
    response = model.generate_content(
        arg,
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        },
    )

    await interaction.response.send_message(response.text)


if __name__ == "__main__":
    bot.run(discord_bot_key)
