#!/usr/bin/python3
"""
Title:				Load Configs
Type:				Helper Module
Purpose:			Load JSON configs
Last Edited By:		AG | MuirlandOracle
Last Updated:		25/03/21
"""

import os, json

with open("config/secret.json") as secretData,\
		open("config/config.json") as generalConf,\
		open("config/rules.json") as rulesHandle,\
		open("config/people.json") as peopleHandle,\
		open("config/logMessages.json") as logs:
	secrets = json.load(secretData)
	rules = json.load(rulesHandle)
	logMsg = json.load(logs)
	people = json.load(peopleHandle)
	config = json.load(generalConf)



def getLog():
	start = os.environ["START-TIME"]
	return f"logs/{start}.log"
