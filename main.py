import sys
from collections import deque

# We can use letters to represent 'numbers' above 9 in base 10, we use this conversation matrix to do so.
letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Set some variables from the commandline arguments.
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <i_num> <o_base>")
    exit()
i_num = int(sys.argv[1])
o_base = int(sys.argv[2])

# We use deque to effectively add characters to the new list
out_deq = deque("")
# Variable 'p' will be used as a container to pass on the value to next digit.
# We will cycle through and check how many times the base can fit inside p,
# we will pass this to the next digit and append the rest to the current
# digit place.
p = i_num
while p > 0:
    # p: how many times do o_base fit inside the our number
    # r: the rest is what actually fits inside the current digit place
    # the overflow from the current digit place will be passed to the next
    # digit place
    p, r = p//o_base, p%o_base
    # the rest 'r' will be added to the current digit place
    out_deq.appendleft(r)

# Convert the array of numbers to a string while converting numbers above 9 to a letter:
# e.g: [1, 15] => 1F
out = ""
for e in out_deq:
    out += letters[e]

# Print our result to the console:
print("Input value " + str(i_num) + " in base 10 equals to " + out + " in base " + str(o_base))
