def solveMeSecond(a,b):
   return a+b

n = int(raw_input())

for i in range(0,n):
    a, b = raw_input().split()
    a,b = int(a),int(b)
    res = solveMeSecond(a,b)
    print res

"""I
2
2 3
3 7
"""

"""O
5
10
"""

"""I
3
1 2
3 7
4 5
"""

"""O
3
10
9
"""
