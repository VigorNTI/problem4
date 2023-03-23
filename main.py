import sys
from collections import deque

# We can use letters to represent 'numbers' above 9 in base 10, we use this conversation matrix to do so.
letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Set some variables from the commandline arguments.
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <i_num> <i_base> <o_base>")
    exit()
i_num = sys.argv[1]
i_base = int(sys.argv[2])
o_base = int(sys.argv[3])

def b10_to_b(num, base):
    # We use deque to effectively add characters to the new list
    out_deq = deque("")
    # Variable 'p' will be used as a container to pass on the value to next digit.
    # We will cycle through and check how many times the base can fit inside p,
    # we will pass this to the next digit and append the rest to the current
    # digit place.
    p = num
    while p > 0:
        # p: how many times do o_base fit inside the our number
        # r: the rest is what actually fits inside the current digit place
        # the overflow from the current digit place will be passed to the next
        # digit place
        p, r = p//base, p%base
        # the rest 'r' will be added to the current digit place
        out_deq.appendleft(r)

    # Convert the array of numbers to a string while converting numbers above 9 to a letter:
    # e.g: [1, 15] => 1F
    # I could have used the ascii table like I did in the b_to_b10 function to
    # convert numbers to letters but I didn't think of it then. This limits the
    # usable characters to A-Z which limits the base output to 36, 0-10 + A-Z
    # which I do find reasonable
    out = ""
    for e in out_deq:
        out += letters[e]
    return out

def b_to_b10(num, base):
    # Convert the digits of the number string to a list of digits
    l = list(num)
    # We start the algorithm from the end so reverse the list is easiest
    l.reverse()
    # Set the output number variable and the digit place variable
    o = 0
    i = 0
    for d in l:
        # Convert the digit from whatever base it is into an integer
        try:
            # If the digit already is a number, just convert it to an int
            d = int(d)
        except:
            # If the digit is a letter, we remove 55 from it's ascii integer
            # representation to get the new number, i.e 'A' in the ascii table
            # is 65, we remove 55 and get 10, which is the next number after 9.
            d = ord(d.upper()) - 55
        # This is the algorithm, multiply each digit with it's base to the power
        # of it's digit place. For example 7061 in base 8 to base 10:
        # 7061(base 8) = (7*8**3) + (0*8**2) + (6*8**1) + (1*8**0) = 3633
        o += d*(base**i)
        # Go to the next digit
        i += 1
    # Return the new number
    return o

print(b10_to_b(b_to_b10(i_num, i_base), o_base))
