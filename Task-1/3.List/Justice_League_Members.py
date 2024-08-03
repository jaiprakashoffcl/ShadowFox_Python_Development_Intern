# Initial list of Justice League members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)
print("\n")

# 1. Calculate the number of members in the Justice League.
number_of_members = len(justice_league)
print("Number of members in the Justice League:", number_of_members)
print("\n")

# 2. Batman recruited Batgirl and Nightwing as new members. Add them to your list.
justice_league.extend(["Batgirl", "Nightwing"])
print("Justice League after adding Batgirl and Nightwing:")
print(justice_league)
print("\n")

# 3. Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Justice League with Wonder Woman as the leader:")
print(justice_league)
print("\n")

# 4. Aquaman and Flash are having conflicts, and you need to separate them.
# Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash.
justice_league.remove("Green Lantern")  # I chose to move Green Lantern
justice_league.insert(justice_league.index("Aquaman") + 1, "Green Lantern")
print("Justice League with Green Lantern between Aquaman and Flash:")
print(justice_league)
print("\n")

# 5. The Justice League faced a crisis, and Superman decided to assemble a new team.
# Replace the existing list with the following new members: "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow".
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("Justice League after Superman assembles a new team:")
print(justice_league)
print("\n")

# 6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
justice_league.sort()
print("Justice League sorted alphabetically with the new leader:")
print(justice_league)
