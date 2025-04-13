import random
from discord.ext import commands

class Randomnumber(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="randomnum", help="Generate a random number and see if you win!")
    async def randomnumber(self, ctx):
        random_value = random.randint(1, 100)
        reward = 0

        if 1 <= random_value <= 20:
            multiplier = 1
            reward = 100_000
        elif random_value == 21:
            multiplier = 3
            reward = 300_000
        elif 22 <= random_value <= 41:
            multiplier = 2
            reward = 200_000
        elif random_value == 42:
            multiplier = 6
            reward = 600_000
        elif 43 <= random_value <= 62:
            multiplier = 3
            reward = 300_000
        elif random_value == 63:
            multiplier = 9
            reward = 900_000
        elif 64 <= random_value <= 83:
            multiplier = 4
            reward = 400_000
        elif random_value == 84:
            multiplier = 12
            reward = 1_200_000
        else:
            multiplier = 0

        if multiplier > 0:
            await ctx.send(f"🎉 You Win! The number was {random_value}. Reward: {reward} credits.")
        else:
            await ctx.send(f"😢 You Lose! The number was {random_value}. Try again.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Randomnumber(bot))
