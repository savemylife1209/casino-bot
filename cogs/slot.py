import discord
import random
from discord.ext import commands

class Slot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="slot")
    async def slot(self, ctx, bet: str):
        """
        Try your luck in the slot!
        bet: The amount to bet. Use 'm' for max and 'a' for all-in.
        """
        payouts = {
            "seven": {3: 500, 2: 25},
            "diamond": {3: 25, 2: 10},
            "bar": {3: 5, 2: 3},
            "bell": {3: 3, 2: 2},
            "shoe": {3: 2, 2: 1},
            "lemon": {3: 1, 2: 1},
            "melon": {3: 0.75, 2: 1},
            "heart": {3: 0.5, 2: 0.75},
            "cherry": {3: 0.5, 2: 0.25},
        }
        items = list(payouts.keys())
        
        # Simulating the slot machine spin
        result = [random.choice(items) for _ in range(3)]
        
        # Count occurrences and calculate the payout
        counts = {item: result.count(item) for item in result}
        best_match = max(counts, key=lambda x: (counts[x], payouts[x].get(counts[x], 0)))
        payout_ratio = payouts[best_match].get(counts[best_match], 0)
        
        # Formatting the result
        slot_display = " | ".join(result)
        await ctx.send(f"**Slot Result:** {slot_display}\n**Payout Ratio:** {payout_ratio}:1")

        # Handle bet calculation (example only)
        if bet.isdigit():
            amount = int(bet)
            payout = amount * payout_ratio
            await ctx.send(f"You bet {amount} and won {payout}!")
        elif bet.lower() in ['m', 'a']:
            await ctx.send("Special bets ('max' or 'all-in') are not implemented yet.")
        else:
            await ctx.send("Invalid bet. Please specify a valid amount or 'm'/'a'.")

async def setup(client: commands.Bot):
    await client.add_cog(Slot(client))