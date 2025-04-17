import discord
import random
from discord.ext import commands
from images.fox.fox_images import image_urls  # Import the URL list

class Fox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fox(self, ctx):
        role_id = 850023963546353734  # Role that grants permission
        role = discord.utils.get(ctx.author.roles, id=role_id)

        if role or ctx.author.id == 793779565050855435:  # Admin check
            if image_urls:
                random_url = random.choice(image_urls)  # Pick a random URL

                # Create an embed with the image
                embed = discord.Embed(title="🦊 AAAAAAAAAAAAAAAAAAAAA 🦊")
                embed.set_image(url=random_url)

                await ctx.send(embed=embed)  # Send the embed
            else:
                await ctx.send("❌ No foxes found! 🦊")
        else:
            await ctx.send("❌ You need to be Level 30 to use this command.")

async def setup(bot):
    await bot.add_cog(Fox(bot))  # Await the add_cog method
