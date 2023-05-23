"""
A set is a collection in which each item must be unique. When you wrap set() around a list that contains duplicate items, Python identifies the unique items in the list and builds a set from those items. You can build a set directly using braces and separating the elements with commas.
"""

######## Building a Set ########
languages = {'python', 'ruby', 'python', 'c'}

# Output -> {'ruby', 'python', 'c'}

"""
Please Note:
It's easy to mistake sets for dictionaries because they're both wrapped in braces.
When you see braces but no key-value pairs, you're probably looking at a set. Unlike
lists and dictionaries, sets do not retain items in any specific order.
"""

