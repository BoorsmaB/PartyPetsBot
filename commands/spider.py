import discord
import random
from discord.ext import commands
from images.spider.spider_images import image_urls  # Import the URL list

class Spider(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spider(self, ctx):
        role_id = 851488903567638549  # Role that grants permission
        role = discord.utils.get(ctx.author.roles, id=role_id)

        if role or ctx.author.id == 793779565050855435:  # Admin check
            if image_urls:
                random_url = random.choice(image_urls)  # Pick a random URL

                # Create an embed with the image
                embed = discord.Embed(title="🕸Pls no kill, I eat bugs🕸")
                embed.set_image(url=random_url)

                await ctx.send(embed=embed)  # Send the embed
            else:
                await ctx.send("❌ No spiders found! 🕷")
        else:
            await ctx.send("❌ You need to be Level 60 to use this command.")

async def setup(bot):
    await bot.add_cog(Spider(bot))  # Await the add_cog method
