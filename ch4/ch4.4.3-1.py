#!/usr/local/bin/python3

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
	number = numbers[position]
	if number %2 == 0:
		print('Found even number', number)
		break
	position += 1
else: #break가 호출되지 않았다.
	print('No even number found')