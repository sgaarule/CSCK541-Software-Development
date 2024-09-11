
# This is python code examples from activity 2.3
# Example 1a
greek_island = "Santorini"

# Example 1b - Assignment operator integer & tuple
earth_age_bln = 4.4
universe_age_bln = 14
earth_age_bln += 0.1

print(earth_age_bln)

# Example 1c - Assignment operator list
asia_wishlist = ["Bhutan", "Ha Long", "Laos", "Danxia", "Seoul", "Khao Sok", "Cebu", "Chiang Mai", "Ho Chi Minh"]

# Example 2a - Relational operator
msg = "life is beautiful"
if msg == "I love you":
    print("propose")
else:
    print("wait xP")

# Example 2b - Relational comparator

net_earnings = 10000000
if net_earnings >= 100000000:
    print("Large Cap")
else:
    print("small Cap")

# Example 3a -  Membership operator
lst = ["soccer", "swimming", "running", "skiing"]
if "rock climbing" not in lst:
    print("boo")

# Example 3b -  Membership operator
web_data = ["techresearch and computervision"]
if any("@" in item for item in web_data):
    print("e-mail address")
elif any(any(char in "0123456789" for char in item) for item in web_data):
    print("phone number")
else:
    print("not e-mail nor phone number")

# Example 4 -  Arithmetic Operator
a = 10 + 20
b = 100 - 1
c = 50 / 7
d = 50 // 7
e = 10 % 8
f = 5 ** 2

print(a, b, c, d, e, f, sep="\n ")