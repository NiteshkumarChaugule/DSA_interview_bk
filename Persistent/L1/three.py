"""
[11:43 am] Sagar Wagh

Given a string, write program to re-arrange all the numbers appearing in the string in decreasing order.

E.g.
Input : I am 7 years and 11 months old
Output : I am 11 years and 7 months old

"""
import re

pattern = "d"
text = "I am 7 years and 11 months old"

for m in re.findall(r"\d.", text):
    print(m)
