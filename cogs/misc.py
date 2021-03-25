#!/usr/bin/python3
"""
Title:				Misc Cog
Type:				Cog
Purpose:			Contains things like the Help command and Github link
Author:				AG | MuirlandOracle
Last Edited By:		AG | MuirlandOracle
Last Updated:		25/03/21
"""
import discord
from discord.ext import commands
from libs.loadconf import config, strings


class Misc(commands.Cog):
	def __init__(self, bot):
		self.bot=bot
	
		#Help command for the bot
		@bot.command(name="help", description="Help Command", usage=f"config['prefix']help")
		async def help(ctx, cmd = None):
			embed = discord.Embed(colour=discord.Colour.blue())
			#Check to see if the user specified a command to get help for
			if cmd != None:
				found = False
				#Check if the command exists but is hidden
				if cmd not in config["hiddenCommands"]:
					for command in bot.commands:
						if cmd == command.name:
							embed.title = f"**{command.name.capitalize()}**"
							embed.description = f"__*Description:*__ ```{command.description}```\n__*Usage:*__ ```{command.usage}```"
							found = True
							break;
				#If the command was hidden (or doesn't exist), send an error
				if not found:
					await ctx.channel.send(strings["errors"]["commandNotFound"].format(cmd))
					return

			#If no argument was given, send all the commands
			else:
				embed.title = "**Help**"
				desc = strings["misc"]["helpDescription"].format(config["prefix"])
				desc += "```"
				for command in bot.commands:
					if command.name not in config["hiddenCommands"]:
						desc += f"\n{command.name}"
				embed.description=f"{desc}```"
			try:
				await ctx.author.send(embed=embed)
				await ctx.message.add_reaction('\U0001F44D')
			except discord.errors.Forbidden:
				await ctx.channel.send(strings["errors"]["noDMs"].format(ctx.message.author.id))


		#Provide a link to the bot's github repo
		@bot.command(name="github", description="Link to the bot Github repo", usage=f"{config['prefix']}github")
		async def github(ctx):
			embed = discord.Embed(colour=discord.Colour.green())
			embed.title = "Github"
			embed.description = config["github"]
			await ctx.channel.send(embed=embed)
		


def setup(bot):
	bot.add_cog(Misc(bot))

