#!/usr/bin/python3
import discord, json, requests, random
from discord.ext import commands

prefix = "!"
bot = commands.Bot(command_prefix=prefix)



#### Connectivity Checks ####
@bot.event
async def on_ready():
	print("Connected Successfully")
	print(bot.user)



@bot.command()
async def ping(ctx):
	await ctx.send("Pong!")







#### Rules ####
@bot.command(name="rules")
async def rules(ctx):
	with open("strings/rules.json", "r") as data:
		rules = json.load(data)
	embed = discord.Embed(colour=discord.Colour.red(), title="Rules:")
	for index, value in enumerate(rules):
		embed.add_field(name=f"__**Rule {index + 1}:**__", value=value)
	
	await ctx.send(embed=embed)


@bot.command(name="rule")
async def rule(ctx, ruleNum):
	try:
		ruleNum = int(ruleNum)
	except:
		await ctx.send(f"{ruleNum} is not a valid integer.")
		return

	with open("strings/rules.json", "r") as data:
		rules = json.load(data)

	try:
		assert(ruleNum < len(rules) and ruleNum > 0)
	except:
		await ctx.send(f"There are {len(rules)} rules. Perhaps you'd like to pick one of those?")
		return

	await ctx.send(f"__Rule {ruleNum}:__ ```{rules[ruleNum - 1]}```")
@rule.error
async def rule_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("This command requires an integer argument")


#### Partners ####
@bot.command(name="partners", aliases=["partner"])
async def partners(ctx, partner=None):
	with open("strings/partners.json", "r") as data:
		partners = json.load(data)

	if not partner:
		for i in partners:
			await ctx.send(i["link"])
		return


	partner = partner.lower()
	for i in partners:
		if partner in i["names"]:
			await ctx.send(i["link"])
			return
	await ctx.send("Nope")


#### Bash Command ####
@bot.command(name="pet", description="Get a pet pic", aliases=["bash", "ollie"])
async def bash(ctx, pet=None):
	pets = ["bash", "ollie"]
	if not pet:
		pet = random.choice(pets)
	else:
		pet = pet.lower()
		if pet not in pets:
			pet = random.choice(pets)

	response = discord.Embed(title=pet.capitalize(), colour=0xff4500)
	r = json.loads(requests.get(f"http://{pet}.muirlandoracle.co.uk").text)
	response.set_image(url=r["message"])
	await ctx.send(embed=response)



if __name__ == "__main__":
	with open("token", "r") as data:
		token = data.read().strip("\n")
	bot.run(token)

