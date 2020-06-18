import random

from discord.ext import commands
from discord.ext.commands import Context, Bot

ZED0_HELP_TEXT = """Very important command."""
FAUX_HELP_TEXT = """A member of the Rust evangelical strike force."""
GO_HELP_TEXT = """The eternal #cs meme."""
DUNNO_HELP_TEXT = """¯\\_(ツ)_/¯"""
RUST_HELP_TEXT = """And if you gaze long into RUST, the RUST also gazes into you."""
PR_HELP_TEXT = """You know what to do"""
ISSUE_HELP_TEXT = """You know what you want someone else to do"""
BLUESHELL_HELP_TEXT = """!blueshell"""
AWOO_HELP_TEXT = """Tails and that"""
SINJO_HELP_TEXT = """o-o"""
TANKSKI_HELP_TEXT = """HONK"""
MGP_HELP_TEXT = """The perfect colour."""


class Misc(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(help=ZED0_HELP_TEXT, brief=ZED0_HELP_TEXT)
    async def zed0(self, ctx: Context):
        await ctx.send("¬_¬")

    @commands.command(help=FAUX_HELP_TEXT, brief=FAUX_HELP_TEXT)
    async def faux(self, ctx: Context):
        await ctx.send("RUST")

    @commands.command(help=GO_HELP_TEXT, brief=GO_HELP_TEXT)
    async def go(self, ctx: Context):
        await ctx.send("lol no generics")

    @commands.command(help=DUNNO_HELP_TEXT, brief=DUNNO_HELP_TEXT)
    async def dunno(self, ctx: Context):
        await ctx.send("¯\\_(ツ)_/¯")

    @commands.command(help=RUST_HELP_TEXT, brief=RUST_HELP_TEXT)
    async def rust(self, ctx: Context):
        await ctx.send("FAUX")

    @commands.command(help=PR_HELP_TEXT, brief=PR_HELP_TEXT)
    async def pr(self, ctx: Context):
        await ctx.send("You can make a pull request for that!")

    @commands.command(help=ISSUE_HELP_TEXT, brief=ISSUE_HELP_TEXT)
    async def issue(self, ctx: Context):
        await ctx.send("You can submit an issue for that!")

    @commands.command(help=BLUESHELL_HELP_TEXT, brief=BLUESHELL_HELP_TEXT)
    async def blueshell(self, ctx: Context):
        await ctx.send(
            "<:blueshell:541726526543101973> Thank you RNGesus for the £5 donation! <:blueshell:541726526543101973>"
        )

    @commands.command(help=AWOO_HELP_TEXT, brief=AWOO_HELP_TEXT)
    async def awoo(self, ctx: Context):
        await ctx.send("Aw{}~".format("o" * random.randrange(2, 5)))

    @commands.command(help=SINJO_HELP_TEXT, brief=SINJO_HELP_TEXT)
    async def sinjo(self, ctx: Context):
        await ctx.send(":neutral_face:")

    @commands.command(help=TANKSKI_HELP_TEXT, brief=TANKSKI_HELP_TEXT)
    async def tankski(self, ctx: Context):
        await ctx.send(":goose:")

    @commands.command(help=MGP_HELP_TEXT, brief=MGP_HELP_TEXT)
    async def mgp(self, ctx: Context):
        await ctx.send("#3D3051")


def setup(bot: Bot):
    bot.add_cog(Misc(bot))
