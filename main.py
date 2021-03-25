#!/usr/bin/python3
"""
Title:				Main
Type:				Main Program
Purpose:			Start the Bot / Load Cogs / etc
Last Edited By:		AG | MuirlandOracle
Last Updated:		24/03/21
"""

import discord, asyncio, signal, os, datetime, sys
from discord.ext import commands
from discord.ext.commands import CommandNotFound, MissingRequiredArgument
from libs.loadconf import secrets, config
from libs.colours import Colours
from libs.logging import Log



#Signal Handling
def exit():
	Log.end()
	sys.exit()

def sigHandle(sig, frame):
	exit()

signal.signal(signal.SIGINT, sigHandle)


#Sort out log directory
if not os.path.isdir("logs"):
	try:
		os.mkdir("logs")
	except:
		Colours.fail("Couldn't create log directory")


#Record the start time for the bot
os.environ["START-TIME"] = str(datetime.date.today())

#Create the bot
bot = commands.Bot(command_prefix=config["prefix"])
bot.remove_command("help")


#Load Cogs
for cog in config["cogs"]:
	if cog not in config["disabledCogs"]:
		try:
			bot.load_extension(f"cogs.{cog}")
			Colours.success(f"{cog} loaded successfully")
		except Exception as e:
			Colours.warn(f"{cog} failed to load: {e}")
	else:
		Colours.info(f"Skipping {cog}")
		

#Sort out basic bot events
@bot.event
async def on_ready():
	if config["status"] != "":
		await bot.change_presence(activity=discord.Game(config["status"]))
	Log.start()


@bot.event
async def on_command_error(ctx, error):
	error_to_skip = [CommandNotFound, MissingRequiredArgument]
	for error_type in error_to_skip:
		if isinstance(error, error_type):
			return
	raise error


#Start the bot
try:
	bot.run(secrets["token"])
except RuntimeError:
	exit()

