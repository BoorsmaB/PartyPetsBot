import discord
import random
from discord.ext import commands
from images.panda.panda_images import image_urls  # Import the URL list

class Panda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def panda(self, ctx):
        role_id = 851488747861835796  # Role that grants permission
        role = discord.utils.get(ctx.author.roles, id=role_id)

        if role or ctx.author.id == 793779565050855435:  # Admin check
            if image_urls:
                random_url = random.choice(image_urls)  # Pick a random URL

                # Create an embed with the image
                embed = discord.Embed(title="🐼🎍 We're just wearing corpse paint! 🎍🐼")
                embed.set_image(url=random_url)

                await ctx.send(embed=embed)  # Send the embed
            else:
                await ctx.send("❌ No panda's found! 🐼")
        else:
            await ctx.send("❌ You need to be Level 35 to use this command.")

async def setup(bot):
    await bot.add_cog(Panda(bot))  # Await the add_cog method
