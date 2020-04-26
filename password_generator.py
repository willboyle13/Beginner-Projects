import random

def length():
	passlen = int(input("How long do you want your password to be? "))
	if passlen >= 4:
		return passlen
	else:
		print('Your password needs to be at least 4 characters!')
		passlen = int(input("How long do you want your password to be? "))
		return passlen
def lowercases():
	letterslow = "abcdefghijklmnopqrstuvwxyz"
	for letters in letterslow:
		return random.choice(letterslow)

def uppercases():
	lettersup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for letterz in lettersup:
		return random.choice(lettersup)

def symbols():
	symbols = "!@#$%^&*()?"
	for syms in symbols:
		return random.choice(symbols)

def numbers():
	numbers = "0123456789"
	for nums in numbers:
		return random.choice(numbers)

passlen = length()
password = []

while len(password) < passlen:
	password.append(lowercases())
	password.append(uppercases())
	password.append(symbols())
	password.append(numbers())
	continue

	if len(password) == passlen:
		break

print(''.join(password))

