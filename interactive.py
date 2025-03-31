#!/bin/python
import math as maths

import default_values



			
			



def print_params(params):
	for param in params:
		print("{}: {}".format(param,params[param]))


def input_loop(params):
	while True:
		i = input("> ")
		args = i.split(" ")
		cmd = args.pop(0)

		if (cmd == "set" and len(args) == 2 and args[0] in params):
			try:
				params[args[0]] = float(args[1])
			except:
				print("Invalid number")
		elif (cmd == "print"):
			print_params(params)
		elif (cmd == "run"):
			return params
		elif (cmd == "exit"):
			exit(0)
		else:
			print("Unknown command.")

		print("")


def run_intro():
	print("**************************************")
	print("Welcome to the car simulator.")
	print("Here are the available parameters, as well as their default values:")
	print("**************************************")
	
	params = default_values.default_params

	print_params(params)

	print("To change a parameter value, please type 'set [parameter name] [new value].'")
	print("To see the current value of the parameters, type 'print'.")
	print("To run the simulator, type 'run'.\n")

	return input_loop(params)


	


