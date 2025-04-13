import random
from discord.ext import commands

class Randomnumber(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="randomnum", help="Generate a random number and see if you win!")
    async def randomnumber(self, ctx):
      
        random_value = random.uniform(0.0, 1.0)
        winning_number = 0.1234567890123456  
        if random_value == winning_number:
            await ctx.send(f"🎉 You Win! The number was {random_value}.")
        else:
            await ctx.send(f"😢 You Lose! The number was {random_value}. Try again.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Randomnumber(bot))
