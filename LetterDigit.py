def letterAndDigit(string):
	if(string=='none' or string==''): return
	digit = []
	let = []
	for letter in string:
		if letter.isdigit():
			digit.append(letter)
		elif letter.isalpha():
		       let.append(letter)
	count = {'Digit':len(digit),'Letter':len(let)}
	return count
		

ans = letterAndDigit("1 year has 12 months. A month has 4 weeks. a week has 7 days.")
print (ans)
