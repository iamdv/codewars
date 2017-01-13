# https://www.codewars.com/kata/exclamation-marks-series-number-17-put-the-exclamation-marks-and-question-marks-to-the-balance-are-they-balanced/train/python



leftString = '!!'
rightString = '??'

def balance(left, right):
	if ((left.count('!') * 2) + (left.count('?') * 3)) == ((right.count('!') * 2) + (right.count('?') * 3)):
		return 'Balance'
	elif ((left.count('!') * 2) + (left.count('?') * 3)) > ((right.count('!') * 2) + (right.count('?') * 3)):
		return 'Left'
	elif ((left.count('!') * 2) + (left.count('?') * 3)) < ((right.count('!') * 2) + (right.count('?') * 3)):
		return 'Right'




print(balance("!!","??") == "Right")
print(balance("!??","?!!") == "Left")
print(balance("!?!!","?!?") == "Left")
print(balance("!!???!????","??!!?!!!!!!!") == "Balance")

balance = lambda * a:['Balance','Left','Right'][cmp(*map(lambda s:2*s.count('!')+3*s.count('?'),a))]
