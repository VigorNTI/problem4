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

def b_to_b10_f(num, base):
    o = 0
    i = 0
    for d in num:
        # Convert the digit from whatever base it is into an integer
        try:
            # If the digit already is a number, just convert it to an int
            d = int(d)
        except:
            # If the digit is a letter, we remove 55 from it's ascii integer
            # representation to get the new number, i.e 'A' in the ascii table
            # is 65, we remove 55 and get 10, which is the next number after 9.
            d = ord(d.upper()) - 55
        # This is basically the same algorithm as above, but with negative
        # exponents for the floating point digits, for example:
        # 13.21(base 16) = (1*16**1) + (3*16**0) + (2*16**-1) + (1*16**-2) = 19.21890625
        # above example includes the integer part however is not included in
        # this function since it's only for the floating part. As a side note
        # there could be a better implementation for the b_to_b10 function to
        # handle floating points as well, just decrement the exponents as we
        # travel through the number. This would eliminate the need for two
        # functions. However I decided to keep it separated for simplicity.
        o += base**-(i + 1) * d
        # Move to the next digit
        i += 1
    return o

def b10_to_b_f(num, base):
    out_deq = deque("")
    # Max number of decimals
    limit = 10

    # Convert the string to a float
    f = float(num)
    for i in range(limit):
        # Remove the integer part and continue with the decimal part
        f = f - int(f)
        # multiply with the new base and keep the rest for next digit 
        f *= base
        out_deq.append(int(f))

    # Convert the array of numbers to a string while converting numbers above 9 to a letter:
    # e.g: [1, 15] => 1F
    out = ""
    for e in out_deq:
        out += letters[e]
    return out


def convert(i_n, i_b, o_b):
    # Check if the input is a floating point or not
    if '.' in i_n:
        # If it is a floating point run the normal algorithm on the integer part
        bef, aft = i_n.split('.')

        # Integer part
        bef = b_to_b10(bef, i_b)
        bef = b10_to_b(bef, o_b)

        # Decimal part - different algorithm, could be interpreted as the
        # opposite of the normal algorithm, check the functions for clarification
        aft = b_to_b10_f(aft, i_b)
        aft = b10_to_b_f(aft, o_b)
        return bef + '.' + aft
    else: 
        # If it is not a floating point just run the normal algorithm
        return b10_to_b(b_to_b10(i_n, i_b), o_b)

print(convert(i_num, i_base, o_base))
