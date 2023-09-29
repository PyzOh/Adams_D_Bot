import discord
from discord.ext import commands


class UserinfoCommand(commands.cogs):


    def _init_(self, bot):
        self.bot = bot

    @commands.Cog.slash_command(name='Userinfo', description='Get info about a User')
    async def userinfo_command(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        embed = discord.Embed







def setup(bot):
    bot.add_cog(UserinfoCommand(bot))