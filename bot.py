import discord
from discord.ext import commands
import os

# Load .env file locally if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # Skip if python-dotenv is not installed (e.g., on Railway)

# Get the token

print("Environment Variables:", dict(os.environ))

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    print("Error: DISCORD_TOKEN is not set!")

# Set up bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents)

# Function to load cogs
async def load_cogs():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            cog_name = f"commands.{filename[:-3]}"
            try:
                await bot.load_extension(cog_name)
                print(f"Loaded cog: {cog_name}")
            except Exception as e:
                print(f"Error loading cog {cog_name}: {e}")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Party Pets!"))
    await load_cogs()
    print(f'Loaded cogs: {bot.cogs}')
    for cog_name in bot.cogs:
        print(f"Cog loaded: {cog_name}")

# Run bot
if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: DISCORD_TOKEN is not set in the environment.")