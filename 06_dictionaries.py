# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band["guitar"])

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key / value pair as tuples
print(band.items())

# verify a key exist
print("vocals" in band)
print("triangle" in band)

# change value
band["vocals"] = "Coverdale"
band.update({"bass": "JPG"})

print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # tuple
print(band)

# delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# dictionaries copy
band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy !")
print(band)
print(band2)

# or use dict() constructor function
band3 = dict(band)
print("Good copy !")
print(band3)

# Nested dictionaries

number1 = {
    "name": "Plant",
    "instrument": "Vocals"
}
number2 = {
    "name": "Page",
    "instrument": "Guidar"
}
band = {
    "number1": number1,
    "number2": number2
}
print(band)
print(band["number1"]["name"])

# Sets

nums = {1, 2, 3, 4}

nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# no duplicate allowed
nums = {1, 2, 2, 3, 4}
print(nums)

# True is a dupe of 1 and False is a dupe of zero
nums = {1, True, 2, False, 3, 0}
print(nums)

# check a value is in a Set
print(2 in nums)

# but you cannot refer to an element in the set with an index porition or a key

# Add a new element to a set
nums.add(8)
print(nums)

# add element from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples, and dictionaris, too.

# Merge two sets to create a new set
one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
[print(mynewset)]

# keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)