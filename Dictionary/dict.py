

def main():
	#	[   python, PPA, LSP, Angular]
	#   [      0    1     2     3]
	fess = [12500,15000,21000,15500]



	print("fees",fess)

	print("Please Enter Batch name:")
	batch = input()

	print("your entered batch name is:",batch)
	if batch == "PPA":
		print("Fess are:",fess[1])
	elif batch == "LSP":
		print("Fees are:",fess[2])
	elif batch == "Python":
		print("Fees are:",fess[0])
	elif batch == "Angular":
		print("Fees are:",fess[3])
	else:
		print("There is no such batch in marvellous")


if __name__ == "__main__":
	main()