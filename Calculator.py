num1 = int(input('Enter first number: '))

num2 = int(0)

while True:
	num2 = input('Enter a number or "exit" to exit the loop: ')
	if num2.lower() == "exit"	:
		break;
		
	if not num2.isdigit():
		print("Invalid!input")
		continue
	else	:
		num2 = int(num2)
		
	sym = input('Enter a symbol: ')
	if (sym == '+')	:
		num1 += num2
	elif (sym == '-') :
		num1 -= num2
	elif (sym == '*'):
		num1 *= num2
	elif (sym == '/') :
		if num2 == 0:
			print ("Cannot divide by zero")
			continue		
			num1 /= num2
	elif (sym == '%'):
		if num2 == 0:
			print ("Cannot mod by zero")
			continue
			num1 %= num2
	else	:
		print("Invalid input!")
		
print ('Result: ', num1)
