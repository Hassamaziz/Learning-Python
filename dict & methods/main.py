# dict1={}
# print(type(dict1))

dict2={"good":"Something pleasant","hello":"A formal greeting","1":"the number one"}
print(dict2["hello"])

marks={"Hassam":79,"Waleed":67,"Talha":56}
print(marks["Hassam"])

# Adding something in dictionaries
marks["Saif"]=95
print(marks)
# .get method saves you from getting an error

# print(marks.get("Hassam aziz")) # Output will be NONE

print(marks.keys())
print(marks.values())
print(marks.items())
