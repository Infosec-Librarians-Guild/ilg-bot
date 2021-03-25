#!/usr/bin/python3
"""
Title:				People Cog
Type:				Cog
Purpose:			Send the partners and lists from the org 
Author:				AG | MuirlandOracle
Last Edited By:		AG | MuirlandOracle
Last Updated:		25/03/21
"""
import discord
from discord.ext import commands
from libs.loadconf import config, people


class People(commands.Cog):
	def __init__(self, bot):
		self.bot=bot
	
	
			
		#### Partners ####
		@bot.command(name="partners", aliases=["partner"])
		async def partners(ctx, partner=None):
			if not partner:
				for i in people["partners"]:
					await ctx.send(i["link"])
				return


			partner = partner.lower()
			for i in people["partners"]:
				if partner in i["names"]:
					await ctx.send(i["link"])
					return
			await ctx.send("Nope")


		#### Bot Contributors ####
		@bot.command(name="contributors", description="List the bot contributors", usage=f"{config['prefix']}contributors")
		async def contributors(ctx):
			contributorList = people["contributors"]
			embed = discord.Embed(colour=discord.Colour.green())
			embed.title = "Bot Contributor List"
			for i in contributorList.keys():
				text = ""
				for j in contributorList[i].keys():
					text += f"__*{j}:*__ {contributorList[i][j]}\n"
				if len(text) == 0:
					text="No socials available"

				embed.add_field(
					name=i,
					value=text,
					inline=False
				)
			await ctx.channel.send(embed=embed)		



def setup(bot):
	bot.add_cog(People(bot))

