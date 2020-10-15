from cs50 import get_int
from math import floor

def main():
    # Initializing variables
    dig1, dig2, num, sum, sum2, result = 0, 0, 0, 0, 0, 0

    # Recieving the number
    cnumber = get_int("Number: ")

    # simple check if its positive
    while cnumber > 0:
        dig2 = dig1
        dig1 = cnumber % 10 #check the rest of the division by 10

        if num % 2 == 0: #if its positive
            sum2 += dig1 #sum the number
        else:
            m = 2 * dig1 #multiplying the second digit
            #the floor division // rounds the result down to the nearest whole number
            sum += (m // 10) + (m % 10) #getting the sum

        cnumber //= 10
        num += 1

    #check the value
    checked = (sum2 + sum) % 10 == 0
    f2digits = (dig1 * 10) + dig2 # first 2 digits

    #printing the results
    if dig1 == 4 and num >= 13 and num <=16 and checked:
        print("VISA\n")
    elif f2digits >= 51 and f2digits <= 55 and num == 16 and checked:
        print("MASTERCARD\n")
    elif (f2digits >= 34 or f2digits == 37) and num == 15 and checked:
        print("AMEX\n")
    else:
        print("INVALID\n")

if __name__ == "__main__":
    main()