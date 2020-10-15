from cs50 import get_int

# Recieve the pyramid's height, while the input is on the defined range
h = 0  #initialing the Height
while (h > 8 or h < 1):
  h = get_int("Height: ")

#print the hashes
for i in range(1, h + 1):
    print( " " * (h-i) + "#"*(i) )