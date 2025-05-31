# Create a set
my_set = set()

# Add elements
my_set.add(1)
my_set.add(2)
my_set.add(3)

# Try to add a duplicate
my_set.add(2)  # This will not add again
print(my_set)
# Check if an element exists
print(2 in my_set)  # True

# Remove an element
my_set.remove(1)

# Print the set
print(my_set)  # Output: {2, 3}
