"""Python refresher course - In Keyword Section"""

friends = ["Minnie", "Darlinda", "Cookie"]

print("Michelle" in friends) # false

# using a set for something like this makes sense because ir prevents us from duplicates & we don't care about the order in which the books have been read
books = {"The Subtle Art of Not Giving A Fuck", "War and Peace", "You're A Badass at Making Money"}
user_book = "War and Peace"

print(user_book in books) #true
