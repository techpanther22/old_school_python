# Write a program that reads numbers until a user enters 55.
# Once 55 is entered, stop reading the input, print out how many numbers have been entered, their total sum, and average
# (do the rounding this way: round(number)).
# Do NOT include 55 in your calculations and print each resulting value on a new line in the order given above.

sumnum = 0
count = 0
us = int(input("ENTER NUMBERS NOT 55:\n"))
while us != 55:
    sumnum += us
    count += 1
    us = int(input())
    continue


print("The count of the numbers: {}".format(count))
print(" The total of numbers entered: " + str(sumnum))
print("The average of the numbrs is: {}".format(round(sumnum / count)))
