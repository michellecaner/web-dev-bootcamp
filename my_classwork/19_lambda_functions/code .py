"""Python refresher course - Lambda Functions Section"""

# this is an unnamed lambda function
# lambda x, y: x + y()

# to get the above to actually do something, you'd need something like this:
print(lambda x, y: x + y(5, 7))