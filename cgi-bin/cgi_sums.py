#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()
nums_to_sum = []
sum = 0

print("Content-type: text/plain")
print("")
form = cgi.FieldStorage()

for x in form:
    nums_to_sum += form.getvalue(x, None)

try:
    for number in nums_to_sum:
        add_num = int(number)
        sum += add_num
        body = "The sum of Operands is: {} ".format(sum)
except (ValueError, TypeError):
    body = "Unable to calculate sum of non-integers"

print(body)
