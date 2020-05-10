number = int(input())
star = 1
for x in range(number):
	print(" "*max(range(number))+"*"*star)
	star += 2
	number -= 1