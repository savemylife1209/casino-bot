import random
from discord.ext import commands

class Randomnumber(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def random_check(self, ctx):
        if random.random() == 0.7777777777777777:
            await ctx.send("You Win!")
        else:
            await ctx.send("You Lose")

async def setup(bot: commands.Bot):
    await bot.add_cog(Randomnumber(bot))

