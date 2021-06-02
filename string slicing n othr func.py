    # in this tutorials we're goin' to learn about string slicing

mystr="shehzad is boy" #string is a combination of characters
print(mystr[4]) #here i can print any specific letter by giving index number
print(mystr[0:8]) #here is 0 will include but 8 will not be included only seven will be included means 0 to 7 will include
print(len(mystr))   #len is a function used to print the length of the given string
print(mystr[0:16:2]) #here, 0 to 16 index means all the character will print on the screen and 2 is means..first 0th index will remain same but after that ek ko leave kerke dusra print hoga character
print(mystr[::3])   #here, two character ko leave kerke third character  print hoga(0th index will remain same)
print(mystr[::-1])  #this statement will print the all string character in reverse direction
print(mystr[-4:])   #here, in negative index will start from the last word of the given character...indexing will start from -1 to ....so on. And rule will be the same like given above

# here are some function
print(type(mystr))
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("boy"))
print(mystr.endswith("bdoy"))
print(mystr.count("e"))
print(mystr.capitalize())
print(mystr.lower())
print(mystr.upper())
print(mystr.find("is"))
print(mystr.replace("is","is a good"))


