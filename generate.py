with open("artifact.txt", "w") as f:
	for i in range(100000):
		print(i, file=f)
