import logging
import discord
from discord.ext import commands
from discord.ext.commands import CheckFailure
from modules.database import *
from modules.views import ConfirmView

logger = logging.getLogger(__name__)
class Reset(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # === Reset ===

    @commands.group()
    async def reset(self, ctx):
        pass

    @reset.command()
    async def char(self, ctx):
        #Do not actually test this until you are done testing and implementing rest of the reset commandline
        view = ConfirmView(ctx.author)

        await ctx.send(
            "Do you really wish to delete your character?",
            view=view
        )

        await view.wait()

        if view.value is None:
            await ctx.send("Timed out.")
        elif view.value:
            await ctx.send("Character deleted.")
            delete_character(ctx.guild.id, ctx.author.id)
        else:
            await ctx.send("Cancelled.")
            
    @reset.command()
    async def stats(self, ctx):
        view = ConfirmView(ctx.author)

        stats = {
            "hp": 0,
            "current_hp": 0,
            "temp_hp": 0,
            "max_hp_bonus": 0,
            "ac": 0,
            "speed": 30,
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10,
            "proficiency": 2,
            "initiative": 0,
            "inspiration": 0,
            "exhaustion": 0,
        }

        await ctx.send("Do you really wish to reset your stats?", view=view)

        await view.wait()

        if view.value is None:
            await ctx.send("Timed out.")
        elif view.value:
            for key, value in stats.items():
                write_character(ctx.guild.id, ctx.author.id, key, value)
            await ctx.send("Stats have been reset.")
        else:
            await ctx.send("Cancelled.")



def setup(bot: commands.Bot):
    bot.add_cog(Reset(bot))