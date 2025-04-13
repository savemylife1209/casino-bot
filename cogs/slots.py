import bisect
import os
import random

import discord
from discord.ext import commands
from modules.economy import Economy
from modules.helpers import *
from PIL import Image


class Slots(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.economy = Economy()

    def check_bet(self, ctx: commands.Context, bet: int=DEFAULT_BET):
        bet = int(bet)
        if bet <= 0 or bet > 100:
            raise commands.errors.BadArgument()
        current = self.economy.get_entry(ctx.author.id)[2]
        if bet > current:
            raise InsufficientFundsException(current, bet)

    @commands.command(
        brief='Slot machine\nbet must be 1-100',
        usage='slots *[bet]'
    )
    async def slots(self, ctx: commands.Context, bet: str="1k"):
        bet = parse_bet(bet)
        self.check_bet(ctx, bet=bet)
        path = os.path.join(ABS_PATH, 'modules/')
        facade = Image.open(f'{path}slot-face.png').convert('RGBA')
        reel = Image.open(f'{path}slot-reel.png').convert('RGBA')

        rw, rh = reel.size
        item = 180
        items = rh // item

        s1 = random.randint(1, items - 1)
        s2 = random.randint(1, items - 1)
        s3 = random.randint(1, items - 1)

        # Payout logic
        payouts = {
            0: (500, 25),  # Seven
            1: (25, 10),   # Diamond
            2: (5, 3),     # Bar
            3: (3, 2),     # Bell
            4: (2, 1),     # Shoe
            5: (1, 1),     # Lemon
            6: (3/4, 1),   # Melon
            7: (1/2, 3/4), # Heart
            8: (1/4, 1/2), # Cherry
        }

        result = ('lost', bet)
        self.economy.add_credits(ctx.author.id, bet * -1)

        if (1 + s1) % 9 == (1 + s2) % 9 == (1 + s3) % 9:
            symbol = (1 + s1) % 9
            reward = payouts[symbol][0] * bet
            result = ('won', reward)
            self.economy.add_credits(ctx.author.id, reward)
        elif (1 + s1) % 9 == (1 + s2) % 9 or (1 + s2) % 9 == (1 + s3) % 9:
            symbol = (1 + s2) % 9
            reward = payouts[symbol][1] * bet
            result = ('won', reward)
            self.economy.add_credits(ctx.author.id, reward)

        embed = make_embed(
            title=(
                f'You {result[0]} {result[1]} credits' +
                ('.' if result[0] == 'lost' else '!')
            ),
            description=(
                'You now have ' +
                f'**{self.economy.get_entry(ctx.author.id)[2]}** ' +
                'credits.'
            ),
            color=(
                discord.Color.red() if result[0] == "lost"
                else discord.Color.green()
            )
        )

        fp = os.path.join(path, 'slot-result.png')  # Define the file path
        facade.save(fp)  # Save the generated image to the file path
        file = discord.File(fp, filename='slot-result.png')
        embed.set_image(url="attachment://slot-result.png")
        await ctx.send(
            file=file,
            embed=embed
        )

        os.remove(fp)

    @commands.command(
        brief=f"Purchase credits. Each credit is worth ${DEFAULT_BET}.",
        usage="buyc [credits]",
        aliases=["buy", "b"]
    )
    async def buyc(self, ctx: commands.Context, amount_to_buy: int):
        user_id = ctx.author.id
        profile = self.economy.get_entry(user_id)
        cost = amount_to_buy * DEFAULT_BET
        if profile[1] >= cost:
            self.economy.add_money(user_id, cost*-1)
            self.economy.add_credits(user_id, amount_to_buy)
        await ctx.invoke(self.client.get_command('money'))

    @commands.command(
        brief=f'Sell credits. Each credit is worth ${DEFAULT_BET}.',
        usage="sellc [credits]",
        aliases=["sell", "s"]
    )
    async def sellc(self, ctx: commands.Context, amount_to_sell: int):
        user_id = ctx.author.id
        profile = self.economy.get_entry(user_id)
        if profile[2] >= amount_to_sell:
            self.economy.add_credits(user_id, amount_to_sell*-1)
            self.economy.add_money(user_id, amount_to_sell*DEFAULT_BET)
        await ctx.invoke(self.client.get_command('money'))

async def setup(client: commands.Bot):
    await client.add_cog(Slots(client))