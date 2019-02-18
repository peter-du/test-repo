"""
Code snippets for HackerRank challenges
"""


# Read input from STDIN
'''
n = int(input())
X = [int(x) for x in input().split()]
Y = [int(x) for x in input().split()]


nm = input().split()
n = int(nm[0])
m = int(nm[1])

l = []

for _ in range(n):
    l.append(list(map(int, input().rstrip().split())))

my_array = numpy.array(l)
'''

# List comprehension + numpy array for matrix multiplication
'''
import numpy

n = int(input())

A = numpy.array([list(map(int, input().rstrip().split())) for _ in range(n)])
B = numpy.transpose(numpy.array([list(map(int, input().rstrip().split())) for _ in range(n)]))

print(numpy.array([[numpy.dot(A[i], B[j]) for j in range(n)] for i in range(n)]))
'''




# Interquartile range
'''
import statistics

n = 30
Xstr = '10 40 30 50 20 10 40 30 50 20 1 2 3 4 5 6 7 8 9 10 20 10 40 30 50 20 10 40 30 50'
Fstr = '1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 10 40 30 50 20 10 40 30 50 20'

X = [int(x) for x in Xstr.split()]
F = [int(x) for x in Fstr.split()]

S = []

for i in range(n):
    S += [X[i]] * F[i]

S.sort()
m = len(S)

lower_half = S[:m//2]

if m % 2 == 1:
    upper_half = S[m//2 + 1:]
else:
    upper_half = S[m//2:]

print(round((statistics.median(upper_half) - statistics.median(lower_half)) * 1.0, 1))
'''


# Minimum Swaps 2
'''
def minimumSwaps(arr):
    n = len(arr)
    numSwaps = 0
    index_dict = {v: i for i,v in enumerate(arr)}
    for i in range(n):
        j = i + 1
        # if j % 10000 == 0:
        #     print('Working on {0:d}'.format(j))
        if arr[i] != j:  # If integer j is not at the right place, do a swap
            idx = index_dict[j]
            arr[idx] = arr[i]
            index_dict[arr[i]] = idx
            arr[i] = j
            index_dict[j] = i
            numSwaps += 1

    return numSwaps


import timeit

f = open('C:\\Users\\Peter\\PycharmProjects\\Temp\\MinimumSwaps2_input10.txt', 'r')

n = int(f.readline().rstrip())

arr = list(map(int, f.readline().rstrip().split()))

print(n, len(arr))

start = timeit.default_timer()

res = minimumSwaps(arr)
print(res)

stop = timeit.default_timer()

print('Time elapsed: {0:.1f} seconds'.format(stop - start))
'''


# Array Manipulation
'''
import timeit

def arrayManipulation(n, queries):
    a = [0] * (n + 1)
    for q in queries:
        a[q[0] - 1] += q[2]
        a[q[1]] -= q[2]

    for i in range(1, len(a)):
        a[i] += a[i-1]

    return max(a)


f = open('C:\\Users\\Peter\\PycharmProjects\\Temp\\ArrayManipulation_input07.txt', 'r')

nm = f.readline().split()
n = int(nm[0])
m = int(nm[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, f.readline().rstrip().split())))

print(n, m)

start = timeit.default_timer()

res = arrayManipulation(n, queries)
print(res)

stop = timeit.default_timer()

print('Time elapsed: {0:.1f} seconds'.format(stop - start))
'''


'''
def primeCount(n):
    prod = 1
    count = 0
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for i in range(15):
        prod *= primes[i]
        count += 1
        if prod > n:
            count -= 1
            break

    return count

x = primeCount(614889782588491400)
print(x)
'''


# Hash Tables: Ransom Note
'''
import timeit
from collections import Counter

def checkMagazine(magazine, note):
    note_word_counts = Counter()
    for w in note:
        note_word_counts[w] += 1
    print('Finished building note word counts')

    magazine_word_counts = Counter()
    for w in magazine:
        magazine_word_counts[w] += 1
    print('Finished building magazine word counts')

    check = True

    for w in note_word_counts:
        if magazine_word_counts.get(w, -1) < note_word_counts[w]:
            check = False
            break

    if check:
        print('Yes')
    else:
        print('No')


f = open('C:\\Users\\Peter\\PycharmProjects\\data\\RansomNote_input16.txt', 'r')

nm = f.readline().split()
n = int(nm[0])
m = int(nm[1])

magazine = f.readline().rstrip().split()
note = f.readline().rstrip().split()

print(n, m, len(magazine), len(note))

start = timeit.default_timer()

checkMagazine(magazine, note)

stop = timeit.default_timer()

print('Time elapsed: {0:.1f} seconds'.format(stop - start))
'''


# Two Strings
'''
def twoStrings(s1, s2):
    res = 'NO'

    for c in s1:
        if c in s2:
            res = 'YES'
            break

    return res

if __name__ == '__main__':
    f = open('C:\\Users\\Peter\\PycharmProjects\\data\\TwoStrings_input05.txt', 'r')

    q = int(f.readline())
    print(q)

    for q_itr in range(q):
        s1 = f.readline().rstrip()
        s2 = f.readline().rstrip()
        print(len(s1), len(s2))

        result = twoStrings(s1, s2)

        print(result)

    f.close()
'''


# Reverse Game
'''
if __name__ == '__main__':
    f = open('C:\\Users\\Peter\\PycharmProjects\\data\\ReverseGame_input04.txt', 'r')

    t = int(f.readline())
    print(t)

    for t_itr in range(t):
        nk = f.readline().rstrip().split()
        n = int(nk[0])
        k = int(nk[1])
        print(n, k)

        k += 1

        if k > n / 2:
            print((n - k) * 2)
        else:
            print(2 * k - 1)

    f.close()
'''


# Sherlock and Divisors
'''
from math import sqrt

def divisors(n):
    if n % 2 == 1:
        return 0

    count = 1
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                count += 1
            if (n // i) % 2 == 0:
                count += 1
            if i == (n // i):
                count -= 1

    return count


print(divisors(861648772))
'''


# Frequency Queries
'''
def freqQuery(queries):
    d = {}
    f = {}
    res = []
    for q in queries:
        if q[0] == 1:
            if d.get(q[1], 0) > 0:
                if f[d[q[1]]] == 1:
                    del f[d[q[1]]]
                else:
                    f[d[q[1]]] -= 1
            d[q[1]] = d.get(q[1], 0) + 1
            f[d[q[1]]] = f.get(d[q[1]], 0) + 1
        elif q[0] == 2:
            if d.get(q[1], 0) > 0:
                if f[d[q[1]]] == 1:
                    del f[d[q[1]]]
                else:
                    f[d[q[1]]] -= 1
                if d[q[1]] == 1:
                    del d[q[1]]
                else:
                    d[q[1]] -= 1
                    f[d[q[1]]] = f.get(d[q[1]], 0) + 1
        elif q[0] == 3:
            x = 0
            if f.get(q[1], 0) > 0:
                x = 1
            res.append(x)

    return res


if __name__ == '__main__':
    f = open('C:\\Users\\Peter\\PycharmProjects\\data\\FrequencyQueries_input07.txt', 'r')

    t = int(f.readline())
    print(t)

    queries = []

    for t_itr in range(t):
        queries.append(list(map(int, f.readline().rstrip().split())))

    freqQuery(queries)

    f.close()
'''


# Even Odd Query

'''
def solve(arr, queries):
    res = []
    n = len(arr)
    for q in queries:
        x = q[0]
        y = q[1]
        if x > y:
            res.append('Odd')
        elif arr[x-1] % 2 == 1:
            res.append('Odd')
        elif arr[x-1] % 2 == 0:
            if x < n and arr[x] == 0 and x != y:
                res.append('Odd')
            else:
                res.append('Even')

    return res


if __name__ == '__main__':
    f = open('C:\\Users\\Peter\\PycharmProjects\\data\\EvenOddQuery_input05.txt', 'r')

    arr_count = int(f.readline())

    arr = list(map(int, f.readline().rstrip().split()))

    q = int(f.readline().rstrip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, f.readline().rstrip().split())))

    res = solve(arr, queries)
    expRes = []
    f2 = open('C:\\Users\\Peter\\PycharmProjects\\data\\EvenOddQuery_output05.txt', 'r')
    for _ in range(q):
        expRes.append(f2.readline().rstrip())

    print(len(res), len(expRes))
    for i in range(q):
        if res[i] != expRes[i]:
            print('i: ', i)
            print('Query: ', queries[i])
            print('A[x]: ', arr[queries[i][0]-1])
            print('res: ', res[i])
            print('expRes: ', expRes[i])

    f.close()
    f2.close()

'''


# Fraudulent Activity Notifications
'''
import os
from statistics import median

def activityNotifications(expenditure, d):
    num = 0
    n = len(expenditure)
    for j in range(d, n):
        if j % 1000 == 0:
            print('Working on: ', j)
        arr = expenditure[j - d:j]
        if expenditure[j] >= median(arr) * 2:
            num += 1

    return num


if __name__ == '__main__':
    f = open('C:\\Users\\Peter\\PycharmProjects\\data\\FraudulentActivityNotifications_input01.txt', 'r')

    nd = f.readline().split()

    n = int(nd[0])
    d = int(nd[1])
    print(n, d)

    expenditure = list(map(int, f.readline().rstrip().split()))

    result = activityNotifications(expenditure, d)
    print(result)

    f.close()
'''


# Special Multiple
'''
def toBinaryList(k):
    res = [int(x) for x in bin(k)[2:]]
    res.reverse()
    return res


def solve(n):
    numDigits = len(str(n))

    while True:
        res = 9 * 10 ** (numDigits - 1)
        for i in range(2 ** (numDigits-1)):
            l = toBinaryList(i)
            k = 0
            m = len(l)
            for j in range(m):
                k += 9 * l[j] * 10**j

            if (res + k) % n == 0:
                res += k
                break

        if res % n == 0:
            break

        numDigits += 1

    return res


ans = solve(463)
print('\nAnswer: ', ans)
'''


# Bus Station
'''
from functools import reduce


def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


# Complete the solve function below.
def solve(a):
    n = len(a)
    m = max(a)
    s = sum(a)
    facs = factors(s)
    facs_to_check = sorted(list(filter(lambda x: x >= m and x < s, facs)))
    res = []
    for f in facs_to_check:
        i = 0
        good_fac = True
        while i < n:
            tot = 0
            for j in range(f):
                tot += a[i+j]
                if tot == f:
                    i += (j+1)
                    break
                elif tot > f:
                    good_fac = False
                    break
            if not good_fac:
                break

        if good_fac:
            res.append(f)

    res.append(s)

    return res


# a = list(map(int, '2 2 1 1 1 1 1 2 1 2'.split()))
a = list(map(int, '1 2 1 1 1 2 1 3'.split()))
print(solve(a))
'''

'''
def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False

    return leap


print(is_leap(2100))
'''


# Primitive Problem
'''
def primitive(p):

    smallest_pr = 0
    num_pr = 0
    found_smallest_pr = False
    for g in range(2, p-1):
        prod = g
        is_pr = True
        for _ in range(p - 3):
            prod = prod * g % p
            if prod == 1:
                is_pr = False
                break

        if is_pr:
            print(g)
            num_pr += 1
            if not found_smallest_pr:
                smallest_pr = g
                found_smallest_pr = True
        else:
            continue

    print(smallest_pr, num_pr)


primitive(443)
'''


def linear_interpolate(n, x_knots, y_knots, x_input):
    # Store the set of points as a list of (x, y) tuples
    points = [(x_knots[i], y_knots[i]) for i in range(n)]

    # By default, Python's list sort() method will sort by ascending x values and ascending y values
    points.sort()

    # We need to find out where x_input lies on our line - then just calculate the line & evaluate it at x_input
    if x_input < points[1][0]:
        p1 = points[0]
        p2 = points[1]
    elif x_input > points[n - 2][0]:
        p1 = points[n - 2]
        p2 = points[n - 1]
    else:
        for i in range(1, n - 1):
            if x_input >= points[i][0] and x_input <= points[i + 1][0]:
                p1 = points[i]
                p2 = points[i + 1]
                break

    print('p1: ', p1)
    print('p2: ', p2)

    # Edge case: x_input = x_p1 and x_input = x_p2
    if x_input == p1[0] and x_input == p2[0]:
        return p1[1]
    # If the line is not vertical, figure out its equation in slope-intercept form
    else:
        m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        b = p1[1] - m * p1[0]
        print(m, b)
        return m * x_input + b

n = 6
x_knots = [-1.0, -1.0, 0.0, 1.0, 2.0, -2.0]
y_knots = [12.0, 10.0, 15.0, 0.0, 5.0, 0.0]
x_input = -0.5

res = linear_interpolate(n, x_knots, y_knots, x_input)
print(res)
