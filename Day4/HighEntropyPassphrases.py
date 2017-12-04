# Day 4 - High-Entropy Passphrases
#
# Task 1
# A new system policy has been put in place that requires all accounts 
# to use a passphrase instead of simply a password. A passphrase 
# consists of a series of words (lowercase letters) separated by spaces.
#
# To ensure security, a valid passphrase must contain no duplicate words.
#
# For example:
#
# aa bb cc dd ee is valid.
# aa bb cc dd aa is not valid - the word aa appears more than once.
# aa bb cc dd aaa is valid - aa and aaa count as different words.

# Task 1
def has_duplicate(list):
    s = []
    for item in list:
        if item in s:
            return True
        s.append(item)
    return False

count = 0
with open("input.txt") as f:
    for line in f:
        list = [(x) for x in line.split()]
        if has_duplicate(list):
        	# This is a false passphras
        	pass
        else:
        	count += 1

print "Task 1: " + str(count)

# Task 2
# For added security, yet another system policy has been put in place. 
# Now, a valid passphrase must contain no two words that are anagrams 
# of each other - that is, a passphrase is invalid if any word's letters 
# can be rearranged to form any other word in the passphrase.
#
# For example:
#
# abcde fghij is a valid passphrase.
# abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
# a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
# iiii oiii ooii oooi oooo is valid.
# oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

# Task 2
def has_anagram(list):
	for item in list:
		for i in list:
			if item != i and sorted(item) == sorted(i):
					return True
	return False
			
count = 0
with open("input.txt") as f:
    for line in f:
        list = [(x) for x in line.split()]
        if has_anagram(list) or has_duplicate(list):
        	# This is a false passphras
        	pass
        else:
        	count += 1

print "Task 2: " + str(count)

