# Write the code to print a literal string saying "Hello World" 
print("Hello World")

# Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a comma in the print function (#2a)
name = "pramila"
print("Hello",name)

# Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a + in the print function (#2b)
name = "pramila"
print("Hello" + name)


#  Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a comma in the print function (#3a)
fav_num = 5
print("Hello",fav_num)

#  Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a + in the print function (#3b)
# fav_num = 5
# print("Hello" +fav_num)

#  NINJA BONUS: Figure out how to resolve the error from above, without changing the + sign to a comma
fav_num = 5
print("Hello" + str(fav_num))

# Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” 
# with the format method (#4a)
food_one = 'burger'
food_two = "momo"
print("I love to eat {} and {}.".format(food_one,food_two))


#  Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}}
#   and {{food_two}}.” with f-strings (#4b)
food_one = 'burger'
food_two = "momo"
print(f"I love to eat {food_one} and {food_two}.")


my_dict = { "name": "Noelle", "language": "Python" }
for key,val in my_dict.items():
     print(key, "=" ,val)



