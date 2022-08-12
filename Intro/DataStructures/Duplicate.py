'''
Task

You are given a string .
Your task is to find the first occurrence of an alphanumeric character in  (read from left to right) that has consecutive repetitions.

Input Format

A single line of input containing the string .

Constraints


Output Format

Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

Sample Input

..12345678910111213141516171820212223
Sample Output

1
Explanation

.. is the first repeating character, but it is not alphanumeric.
1 is the first (from left to right) alphanumeric repeating character of the string in the substring 111.
'''
import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)
