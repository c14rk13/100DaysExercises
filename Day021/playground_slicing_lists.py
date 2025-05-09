piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

# Get only from 3 first values:
print(piano_keys[:3]) # Note that the +1 added to the list index (non-inclusive)


# Get only from 2nd position to the last:
print(piano_keys[1:]) # indicate the position's index (inclusive)


# Get only from 3rd to 5th position:
print(piano_keys[2:5]) # Again, ending position is non-inclusive

# Get only every other key from 3rd to 5th position:
print(piano_keys[2:5:2])

# Get only every other key from the start of the list to the end:
print(piano_keys[::2])


# Reverse the list:
print(piano_keys[::-1])

# Get every other key from the end of list to the start
print(piano_keys[::-2])

# Get 6th position, reverse, then get up to index 2 (hurts my brain!)
print(piano_keys[5:2:-1])