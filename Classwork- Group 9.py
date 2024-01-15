#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Print the first Natural numbers

for i in range(1, 11):
    print(i)


# In[2]:


print("====The First 10 Natural Numbers====")

for i in range(1, 11):
    print(i)


# In[3]:


# Count the total number of digits in a number
number = int(input('Enter a number: '))

# Convert the number to string then get the lenght of the number

num_words = str(number)
num_digits = len(num_words)
print(f"The total number of digits in {number} is: {num_digits}")


# In[7]:


# Write a program to display all prime numbers within a range

num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num < 2:
    print(f"{num} is not a prime number")
else:
    # check for factors
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            flag = True
            break

    # check if flag is True
    if flag:
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")


# In[10]:


# Write a program to print a multiplication table of a given number
number = int(input('Enter number: '))

# Print multiplication table of number

print(f"Multiplication table of {number}: ")

for i in range(1,21):
    result = number * i
    print(f"{number} * {i} = {result}")


# # THE END
