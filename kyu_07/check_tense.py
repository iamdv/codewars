# https://www.codewars.com/kata/check-the-string-tense/train/python

def check_tense(word):
    if(word[-2:] == 'ed'):
        return 'Past'
    else:
        print(word[-2:])
        return 'Present'

check_tense('Loved')
