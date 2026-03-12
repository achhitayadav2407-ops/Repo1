# 1️⃣ Write a Python program to create a dictionary with 5 student names and their marks.

students = {"Achhi":60, "kajal":46, "swati":78, "priyanka":99, "asma":98}
print(students)

# 2️⃣ Write a program to access the value of a specific key in a dictionary.

students = {"Achhi":60, "kajal":46, "swati":78, "priyanka":99, "asma":98}
print(students["swati"])

# 3️⃣ Write a program to add a new key-value pair to an existing dictionary.

students = {"Achhi":60, "kajal":46, "swati":78, "priyanka":99, "asma":98}
students["payal"]= 55
print(students)

# 4️⃣ Write a Python program to update the value of a key in a dictionary.

students = {"Achhi":60, "kajal":46, "swati":78, "priyanka":99, "asma":98}
students["asma"]= 68
print(students)

# 5️⃣ Write a program to remove a key from a dictionary.

students = {"Achhi":60, "kajal":46, "swati":78, "priyanka":99, "asma":98}
students.pop("kajal")
print(students)

# 6️⃣ Write a Python program to check whether a key exists in a dictionary.
students = {"Achhi":60, "kajal":46, "swati":78, "priyanka":99, "asma":98}
if "priyanka" in students:
    print("yes")
else:
    print("No")  

# 7️⃣ Write a program to print all keys and values of a dictionary using a loop.
students = {"Achhi":60, "kajal":46, "swati":78, "priyanka":99, "asma":98}
for key, value in students.items():
    print(key, value)

# 8️⃣ Write a Python program to count the frequency of each character in a string using a dictionary.

text = "Achhi"
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)


# Example string: "python"

# 9️⃣ Write a Python program to merge two dictionaries into one dictionary.

dict1 = {1 : 45, 2: 36, 3: 20}
dict2 = {4 : 54, 5: 63, 6: 23}
dict1.update(dict2)
print(dict1)

# 🔟 Write a Python program to find the key with the maximum value in a dictionary.

dict1 = {1 : 45, 2: 36, 3: 20}
max_value = 0
max_key = None

for key, value in dict1.items():
    if value  > max_value:
        max_value = value
        max_key = key
print(max_key, ":", max_value)

# OR 
dict1 = {1: 45, 2: 36, 3: 20}

max_value = 0
max_key = None

for key, value in dict1.items():
    if value > max_value:
        max_value = value
        max_key = key

print(max_key, ":", max_value)

# for i in dict1:
#     if i > max:
#         max = i
# print(max)  


# Write a program to print all keys of a dictionary.
dict = {1:34, 2:33, 3:35}
print(dict.keys())


# Write a program to print all values of a dictionary.
dict = {1:34, 2:33, 3:35}
print(dict.values())

# Write a program to print all key-value pairs using a loop.
dict = {1:34, 2:33, 3:35}

for key, value in dict.items():
    break
print(dict)

# Write a Python program to check whether a key exists in a dictionary.
dict = {1:34, 2:33, 3:35}

key = int(input("enter any key: "))

if key in dict:
    print("yes")
else:
    print("No")    

# Write a Python program to merge two dictionaries.
dict = {1:34, 2:33, 3:35}
dict1 = {4: 45, 5: 36, 6: 20}
dict.update(dict1)
print(dict)


# Write a Python program to count the frequency of each character in a string using a dictionary.

# Write a Python program to find the key with the maximum value in a dictionary.

# Write a Python program to find the key with the minimum value in a dictionary.

# Write a Python program to sum all the values in a dictionary.

# Write a Python program to sort a dictionary by its keys.

# Write a Python program to sort a dictionary by its values.

# Write a Python program to create a dictionary from two lists.      
