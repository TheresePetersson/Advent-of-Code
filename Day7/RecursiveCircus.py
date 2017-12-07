# Day 7 - Recursive Circus
#
####### Task 1 #######
#One program at the bottom supports the entire tower. It's holding a large disc, 
# and on the disc are balanced several more sub-towers. At the bottom of these 
# sub-towers, standing on the bottom disc, are other programs, each holding their
# own disc, and so on. At the very tops of these sub-sub-sub-...-towers, many 
# programs stand simply keeping the disc below them balanced but with no disc of their own.
#
# You offer to help, but first you need to understand the structure of these towers. 
# You ask each program to yell out their name, their weight, and (if they're holding 
# a disc) the names of the programs immediately above them balancing on that disc. 
# You write this information down (your puzzle input). Unfortunately, in their panic, 
# they don't do this in an orderly fashion; by the time you're done, you're not sure 
# which program gave which information.
#
# For example, if your list is the following:
#
# pbga (66)
# xhth (57)
# ebii (61)
# havc (66)
# ktlj (57)
# fwft (72) -> ktlj, cntj, xhth
# qoyq (66)
# padx (45) -> pbga, havc, qoyq
# tknk (41) -> ugml, padx, fwft
# jptl (61)
# ugml (68) -> gyxo, ebii, jptl
# gyxo (61)
# cntj (57)
# ...then you would be able to recreate the structure of the towers that looks like this:
#
#                gyxo
#              /     
#         ugml - ebii
#       /      \     
#      |         jptl
#      |        
#      |         pbga
#     /        /
# tknk --- padx - havc
#     \        \
#      |         qoyq
#      |             
#      |         ktlj
#       \      /     
#         fwft - cntj
#              \     
#                xhth
# In this example, tknk is at the bottom of the tower (the bottom program), 
# and is holding up ugml, padx, and fwft. Those programs are, in turn, holding up 
# other programs; in this example, none of those programs are holding up any other 
# programs, and are all the tops of their own towers. (The actual tower balancing 
# in front of you is much larger.)
#
# Before you're ready to help them, you need to make sure your information is 
# correct. What is the name of the bottom program?

#Task 1
dct = {}
bottom_program = "-1"

with open("input.txt") as f:
    for line in f:
        lst = [x for x in line.split()]
        if len(lst)>2:
          # remove the ',' for all elements except the last one that doesn't have it
          for index in range(3,len(lst)-1):
            lst[index] = lst[index][:-1]
          # delete "->"
          del lst[2]
        # delete "(" and ")" and make the weight an int
        lst[1] = int(lst[1][1:-1])
        dct[lst[0]] = lst[1:]

# Find bottom_program, the one that doesn't exist in the values of the dct
for key in dct:
  if len(dct[key]) > 1:
    found = False
    for key_2 in dct:
      if len(dct[key_2]) > 1:
        if key in dct[key_2]:
          found = True
          break
    if not found:
      bottom_program = key
      break

print "Task 1: " + bottom_program

####### Task 2 #######
# For any program holding a disc, each program standing on that disc forms a sub-tower.
# Each of those sub-towers are supposed to be the same weight, or the disc itself isn't 
# balanced. The weight of a tower is the sum of the weights of the programs in that tower.
#
# In the example above, this means that for ugml's disc to be balanced, gyxo, ebii, and 
# jptl must all have the same weight, and they do: 61.
#
# However, for tknk to be balanced, each of the programs standing on its disc and all 
# programs above it must each match. This means that the following sums must all be the same:
#
# ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
# padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
# fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
# As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the other two.
# Even though the nodes above ugml are balanced, ugml itself is too heavy: it needs to be 8 
# units lighter for its stack to weigh 243 and keep the towers balanced. If this change were made, 
# its weight would be 60.

# Task 2
def calculateWeight(key):
  weight = 0
  for string in dct[key][1:]:
    weight += calculateWeight(string)
  weight += dct[key][0]
  return weight


def findFalseWeight(key):
  false_key = -1
  weights = []
  right_weight = -1
  for string in dct[key][1:]:
    w = calculateWeight(string)
    if w in weights:
      right_weight = w
    else:
      weights.append(w)
  if len(weights) > 1:
    for w in weights:
      if w != right_weight:
        wrong_weight = w
    for string in dct[key][1:]:
      if calculateWeight(string) == wrong_weight:
        false_key = string
  return false_key

weight = -1
false_key = bottom_program
last_key = ""
while false_key != -1:
  second_last_key = last_key
  last_key = false_key
  false_key = findFalseWeight(false_key)

correct_weight = calculateWeight(dct[second_last_key][1])
weight = calculateWeight(last_key)-correct_weight
weight = dct[last_key][0] - weight


print "Task 2: " + str(weight)
