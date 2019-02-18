# Scratchpad for testing code

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     print(words[2])


# Assignment 8.4

# fh = open("romeo.txt")
# lst = list()
# for line in fh:
#     words = line.rstrip().split()
#     for w in words:
#         if w not in lst:
#             lst.append(w)
# lst.sort()
# print(lst)


# Assignment 8.5

# fname = "mbox-short.txt"
# fh = open(fname)
# count = 0
# for line in fh:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     print(words[1])
#     count += 1
# print("There were", count, "lines in the file with From as the first word")


# Assignment 9.4
# fname = "mbox-short.txt"
# fh = open(fname)
# counts = dict()
# for line in fh:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     counts[words[1]] = counts.get(words[1], 0) + 1
#
# maxCount = 0
# maxName = ""
# for name,count in counts.items():
#     if count > maxCount:
#         maxCount = count
#         maxName = name
#
# print(maxName, maxCount)


# Assignment 10.2
# fh = open("mbox-short.txt")
# counts = dict()
# for line in fh:
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     times = words[5].split(':')
#     hour = times[0]
#     counts[hour] = counts.get(hour, 0) + 1
#
# lst = sorted(counts.items())
# for k,v in lst:
#     print(k,v)


# import re
#
# fh = open("regex_sum_293066.txt")
# # fh = open("regex_sum_42.txt")
# all_nums = list()
# for line in fh:
#     lst = re.findall('[0-9]+', line)
#     all_nums += lst
# print("The sum of %d numbers is %d" % (len(all_nums), sum(map(int, all_nums))))


# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.py4inf.com', 80))
# mysock.send(b'GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode("utf-8"))
#
# mysock.close()


# import urllib.request
#
# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fhand:
#     print(line.decode("utf-8").strip())


# import urllib.request
# from bs4 import BeautifulSoup
#
# # url = "http://python-data.dr-chuck.net/comments_42.html"
# # url = "http://www.dr-chuck.com/page1.htm"
# url = "http://python-data.dr-chuck.net/comments_293071.html"
# html = urllib.request.urlopen(url).read()
#
# soup = BeautifulSoup(html, "html.parser")
# tags = soup('span')
# nums = list()
# for tag in tags:
#     nums.append(int(tag.contents[0]))
# print(len(nums), sum(nums))


# import urllib.request
# from bs4 import BeautifulSoup
#
# # url = "http://python-data.dr-chuck.net/known_by_Fikret.html"
# url = input("Enter URL: ")
# count = input("Enter count: ")
# pos = input("Enter position: ")
#
# for i in range(1, int(count) + 1):
#     print("Retrieving: ", url)
#     html = urllib.request.urlopen(url).read()
#     soup = BeautifulSoup(html, "html.parser")
#     tags = soup('a')
#     url = tags[int(pos) - 1].get('href', None)
#
# print("Retrieving: ", url)


# import urllib.request
# import xml.etree.ElementTree as ET
#
# url = input('Enter location: ')
# print('Retrieving', url)
# uh = urllib.request.urlopen(url)
# data = uh.read()
# print('Retrieved', len(data), 'characters')
# tree = ET.fromstring(data)
#
# counts = tree.findall('.//count')
# counts_int = []
# for count in counts:
#     counts_int.append(int(count.text))
#
# print("Count:", len(counts_int))
# print("Sum:", sum(counts_int))


# import urllib.request
# import json
#
# url = input('Enter location: ')
# print('Retrieving', url)
# uh = urllib.request.urlopen(url)
# data = uh.read().decode('utf-8')
# print('Retrieved', len(data), 'characters')
#
# info = json.loads(data)
# print('Count:', len(info['comments']))
# counts = [item['count'] for item in info['comments']]
# print('Sum:', sum(counts))


import json
import urllib.request
import urllib.parse

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'sensor': 'false', 'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode('utf-8')
    print('Retrieved', len(data), 'characters')

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print("Place id", js['results'][0]['place_id'])



'''
def minimumMoves(a, m):
    numMoves = 0
    n = len(a)
    for i in range(n):
        ai = list(map(int, str(a[i])))
        mi = list(map(int, str(m[i])))
        k = len(ai)
        numMoves += sum([abs(ai[j] - mi[j]) for j in range(k)])

    return numMoves


a = [1234, 4321]
m = [2345, 3214]

ans = minimumMoves(a, m)

print(ans)
'''

'''
def connectedCities(n, g, originCities, destinationCities):
    q = len(originCities)
    if g == 0:
        return [1] * q

    m = []
    for j in range(g+1, n//2 + 1):
        m += [j*k for k in range(1, n//j + 1)]

    clique = set(m)
    print('Clique: ', clique)

    res = []
    for i in range(q):
        o = originCities[i]
        d = destinationCities[i]
        if o not in clique or d not in clique:
            res.append(0)
        else:
            res.append(1)

    return res
'''


'''
def collect_max(mat):
    # Write your code here  
    n = len(mat)
    # Check off-diagonal of -1's for no path
    noPath = False
    for i in range(n):
'''