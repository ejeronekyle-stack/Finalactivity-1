# Part 2: Manipulation Challenge

# -------- LIST TASKS --------
print("=== LIST TASKS ===")
tasks = ["study", "exercise", "cook", "clean", "sleep"]
print("Original List:", tasks)

# Add a new task
tasks.append("review notes")
print("After Adding Task:", tasks)

# Remove one task
tasks.remove("cook")   # removes "cook"
print("After Removing Task:", tasks)

# Sort the list
tasks.sort()
print("After Sorting:", tasks)


# -------- TUPLE TASKS --------
print("\n=== TUPLE TASKS ===")
fruits = ("apple", "banana", "mango", "grapes", "orange")
print("Original Tuple:", fruits)

# Try to change one value
try:
    fruits[1] = "pineapple"   # attempt to change "banana"
except TypeError as e:
    print("Error when modifying tuple:", e)

print("Explanation: Tuples are immutable, meaning their elements cannot be changed after creation.")

# -------- SET TASKS --------
print("\n=== SET TASKS ===")
numbers = {1, 2, 3, 4, 5}
print("Original Set:", numbers)

# Add a number
numbers.add(6)
print("After Adding 6:", numbers)

# Remove a number
numbers.remove(3)
print("After Removing 3:", numbers)

# Show how duplicates are removed
duplicate_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(duplicate_list)
print("Duplicates Removed:", unique_set)

# -------- DICTIONARY TASKS --------
print("\n=== DICTIONARY TASKS ===")
student = {"name": "Jerone", "age": 20, "course": "BSIT"}
print("Original Dictionary:", student)

# Add a new key "grade"
student["grade"] = "A"

# Update "age"
student["age"] = 21

# Print all keys and values
print("Updated Dictionary:", student)
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
