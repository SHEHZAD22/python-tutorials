# Dictionary is nothing but key value pairs. dictionary ko hum braces mein rakhte hain
d1={}
# print(type(d1))
# d2={"shehzad":"burger","bilal":"pizza","sarfraj":"egg roll"}
# print(d2)
# print(d2["shehzad"])

# we can create a dictionaryy inside the dictionary..like given below
d2={"shehzad":"burger","bilal":"pizza",
    "sarfraj":{"b":"maggie","l":"roti","d":"chicken"}}
# print(d2["sarfraj"])
# print(d2["sarfraj"]["b"])

    # to add the elements in the dictionary we do like given below
# d2["sahraj"]="junk food"
# d2["intzar"]="kabab"
# del d2["intzar"]    #del function is used to delete the specific elements that we want to delete

# d3=d2.copy()    #copy function: copied the given dictionary to any other variables...or wo dictionary copy ho jaati hai us dusre variables ko or pehli wali dictionary per koi effect nhi padta hai.
# del d3["shehzad"]
# print(d2)
# print(d3)

# print(d2.get("bilal"))  #get function: is used to get the element
# d2.update({"lina":"coffee"})    #update: update the dictionary by adding
# print(d2)
print(d2.keys())
print(d2.items())