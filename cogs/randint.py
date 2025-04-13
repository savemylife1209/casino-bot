import random
from discord.ext import commands

class Randint(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def random_check(self, ctx):
        number = random.uniform(0, 1)  # Generate a random float between 0 and 1
        if 0.7777 <= number <= 0.7783:  # Check if the number is approximately 0.7777777
            await ctx.send("You Win!")
        else:
            await ctx.send("You Lose!")

async def setup(bot: commands.Bot):
    await bot.add_cog(Randint(bot))
