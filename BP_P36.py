# Concatenate following Dictionary & create new one
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

print("Dictionary 1 is: ", dic1) 
print("Dictionary 2 is: ", dic2) 
print("Dictionary 3 is: ", dic3) 

# empty dictionary
dic4 = {}

print("Empty Dictionary 4 is: ", dic4)

# concatenate

for d in (dic1, dic2, dic3):
    dic4.update(d)                  # update() function

print("After Concatenation Dictionary 4 is: ", dic4) 

# Thanks for Watching
