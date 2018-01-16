'''
Put all teams numbers in teams
'''
import os
import re
def main():
    exp = re.compile(r'[0-999999999999]')
    a = []
    with open('teams.txt') as f:
        lines = f.readlines()
        for line in lines:
            if re.match(exp, line.strip()):
                a.append(int(line.strip()))
    a.sort()
    print(a)
    b = []
    i = 0
    h = 1
    print(len(a))
    while i + 1 < len(a):
        if a[i] == a[i + 1]:
            b.append(a[i])
        i += 1
    print(b)

main()
