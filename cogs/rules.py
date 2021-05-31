#!/usr/bin/python3
"""
Title:				Rules Cog
Type:				Cog
Purpose:			Send the rules on demand
Author:				AG | MuirlandOracle
Last Edited By:		AG | MuirlandOracle
Last Updated:		25/03/21
"""
import discord
from discord.ext import commands
from libs.loadconf import config, rules as ruleList


class Rules(commands.Cog):
	def __init__(self, bot):
		self.bot=bot


		@bot.command(name="rules", description="Send the full rules", usage=f"{config['prefix']}rules")
		async def rules(ctx):
			embed = discord.Embed(colour=discord.Colour.red(), title="Rules:")
			for index, value in enumerate(ruleList, start=1):
				embed.add_field(name=f"__**Rule {index}:**__", value=value, inline=False)
		
			await ctx.send(embed=embed)


		
		@bot.command(name="rule", description="Send a single rule", usage=f"{config['prefix']}rule NUMBER")
		async def rule(ctx, ruleNum):
			try:
				ruleNum = int(ruleNum)
			except:
				await ctx.send(f"{ruleNum} is not a valid integer.")
				return

			try:
				assert(ruleNum <= len(ruleList) and ruleNum > 0)
			except:
				await ctx.send(f"There are {len(ruleList)} rules. Perhaps you'd like to pick one of those?")
				return

			await ctx.send(f"__Rule {ruleNum}:__ ```{ruleList[ruleNum - 1]}```")
		@rule.error
		async def rule_error(ctx, error):
			if isinstance(error, commands.MissingRequiredArgument):
				await ctx.send("This command requires an integer argument")



def setup(bot):
	bot.add_cog(Rules(bot))

