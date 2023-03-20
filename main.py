import sys
from collections import deque

letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <i_num> <o_base>")
    exit()
i_num = int(sys.argv[1])
o_base = int(sys.argv[2])

out_deq = deque("")
p = i_num
while p > 0:
    p, r = p//o_base, p%o_base
    out_deq.appendleft(r)

out = ""
for e in out_deq:
    out += letters[e]

print("Input value " + str(i_num) + " in base 10 equals to " + out + " in base " + str(o_base))
