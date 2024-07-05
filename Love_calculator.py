name1 = input("please enter first name? ")
name2 = input("please enter second name? ")

combined_name = name1 + name2

lower_combined_name = combined_name.lower()

t = lower_combined_name.count("t")
r = lower_combined_name.count("r")
u = lower_combined_name.count("u")
e = lower_combined_name.count("e")

first_digit = t + r + u + e

l = lower_combined_name.count("l")
o = lower_combined_name.count("o")
v = lower_combined_name.count("v")
e = lower_combined_name.count("e")

second_digit = l + o + v + e

love_percentage = int(str(first_digit) + str(second_digit))

if (love_percentage < 10) and (love_percentage > 90):
    print(f"Your love score is {love_percentage}, you both are made for each other")
elif (love_percentage <= 40 ) or (love_percentage >= 50):
    print(f"Your love score is {love_percentage}, have faith in love.")
else:
    print(f"Your love score is {love_percentage}, marry another girl.")