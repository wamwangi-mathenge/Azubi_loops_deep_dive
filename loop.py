s = "abcd"

# print all the letters in s:
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print()
# This code violates the principle of DRY = Don't Repeat Yourself

# For loop - Let's repeat the same code a number of times, with slight variation each time
# What's the variation? Each time, we'll get a different character from s, our string

s = "abcd"

for one_letter in s: 
    print(one_letter)
    
print()    
for one_item in [10, 20, 30]:
    print(one_item)
    
print()    
    
# How can I iterate over s, using the length/index?

for i in range(len(s)):
    print(s[i])
    
# This is unnecessary in Python
print()

## Range

## What do we get from range in each iteration

for one_item in range(3):
    print(f"{one_item}: Hooray!!!")
    
print()
    
for index in range(len(s)):
    print(f"{s[index]}")
    
    
print()

## Calling range with two elements

for one_number in range(10, 15):
    print(one_number)
    
print()

## Calling range with 3 elements

for one_number in range(20, 30, 2):
    print(one_number)
    
print()

## Counting backwards
for one_number in range(30, 20, -1):
    print(one_number)
    
print()

## Enumerate
for one_item in enumerate(s):
    print(one_item)