import random

# Variables to store statistics
roll_6_count = 0
roll_1_count = 0
two_6_in_a_row_count = 0

# Simulating rolling a six-sided die at least 20 times
for _ in range(20):
    roll = random.randint(1, 6)
    print("Roll:", roll)

    # Counting statistics
    if roll == 6:
        roll_6_count += 1
    if roll == 1:
        roll_1_count += 1
    if roll == 6 and previous_roll == 6:
        two_6_in_a_row_count += 1

    previous_roll = roll

# Printing statistics
print("Number of times rolled a 6:", roll_6_count)
print("Number of times rolled a 1:", roll_1_count)
print("Number of times rolled two 6s in a row:", two_6_in_a_row_count)
