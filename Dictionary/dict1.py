

def main():
	#	[   python, PPA, LSP, Angular]
	#   [      0    1     2     3]
	# fess = [12500,15000,21000,15500]

	fess = {"python":12500,"PPA":15000,"LSP":21000,"Angular":15500}



	print("fees",fess)

	print("Please Enter Batch name:")
	batch = input()


	print("Thank you for selcting batch",batch)
	print("Fees are:",fess[batch])


if __name__ == "__main__":
	main()