import random 
# The actual code
hm = input("how much letters ? ")
if hm == "1":
    print(random.randrange(0, 10))
if hm == "2":
    print(random.randrange(0, 100))
if hm == "3":
    print(random.randrange(0, 1000))
if hm == "random" :
    print(random.randrange(0, 10000))
