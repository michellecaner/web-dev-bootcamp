"""Python refresher course - Adv Set Ops Section"""

# using .difference
friends = {"Stephanie", "Megan", "Alyssa"}
abroad = {"Stephanie", "Alyssa"}

# here we are starting with the friends set and asking for the difference from the abroad set - that value is assigned to the local_friends variable
local_friends = friends.difference(abroad)

print(local_friends)

# using .union
local = {"Michelle"}
abroad = {"Stephanie", "Alyssa"}

# unites two sets
friends = local.union(abroad)

print(friends)

# using .intersection
art = {"Tara", "Rebecca", "Michelle", "Simone"}
science = {"Rebecca", "Paolo", "Simone", "Daniella"}

both = art.intersection(science)

print(f"{both} take art and science.")