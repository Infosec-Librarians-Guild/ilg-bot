#!/usr/bin/python3
"""
Title:				Logging
Type:				Helper Module
Purpose:			Log all the things
Last Edited By:		AG | MuirlandOracle
Last Updated:		24/03/21
"""
from datetime import datetime
from libs.colours import Colours
from libs.loadconf import getLog, logMsg





class Log():
	date = lambda: datetime.utcnow()

		

	#Write to file
	@classmethod
	def writeToFile(self, msg):
		with open(getLog(), "a") as handle:
			handle.write(f"{msg}\n")



	#### Log Functions ####
	@classmethod
	def start(self):
		Colours.success("Logging Enabled")
		self.writeToFile(logMsg["start"].format(self.date()))

	@classmethod
	def end(self):
		self.writeToFile(logMsg["end"].format(self.date()))	


	@classmethod
	def cogLoad(self, res, cog, error = None):
		if res == "success":
			Colours.success(f"Loaded {cog} cog successfully")
			self.writeToFile(logMsg["cogSuccess"].format(self.date(), cog))
		else:
			Colours.fail(f"Failed to load cog: {cog}.\n{error}")
			self.writeToFile(logMsg["cogFail"].format(self.date(), cog))
