from itertools import product

K,M = input().split(" ")
K,M = int(K),int(M)

# N = (list(map(int, input().split()))[1:] for _ in range(K))
# results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
# print(list(results))

arr = []

for i in range(K):

    arr.append(list(map(int, input().split()))[1:])

m_arr = product(*arr)

max_sum = []
for i in m_arr:
    print(i)
    print(sum(x**2 for x in i))
    _sum = max_sum.append(sum(x**2 for x in i)%M)


print(sorted(max_sum))
print(max(max_sum))

'''
7 867
7 6429964 4173738 9941618 2744666 5392018 5813128 9452095
7 6517823 4135421 6418713 9924958 9370532 7940650 2027017
7 1506500 3460933 1550284 3679489 4538773 5216621 5645660
7 7443563 5181142 8804416 8726696 5358847 7155276 4433125
7 2230555 3920370 7851992 1176871 610460 309961 3921536
7 8518829 8639441 3373630 5036651 5291213 2308694 7477960
7 7178097 249343 9504976 8684596 6226627 1055259 4880436
'''
'''
6 767
2 488512261 423332742
2 625040505 443232774
1 4553600
4 92134264 617699202 124100179 337650738
2 778493847 932097163
5 489894997 496724555 693361712 935903331 518538304

[247, 527, 396, 368, 423, 125, 405, 274, 246, 301, 749, 262, 131, 103, 158, 627, 140, 9, 748, 36, 518, 31, 667, 639, 694, 396, 676, 545, 517, 572, 223, 503, 372, 344, 399, 101, 381, 250, 222, 277, 278, 558, 427, 399, 454, 156, 436, 305, 277, 332, 13, 293, 162, 134, 189, 658, 171, 40, 12, 67, 549, 62, 698, 670, 725, 427, 707, 576, 548, 603, 254, 534, 403, 375, 430, 132, 412, 281, 253, 308, 434, 714, 583, 555, 610, 312, 592, 461, 433, 488, 169, 449, 318, 290, 345, 47, 327, 196, 168, 223, 705, 218, 87, 59, 114, 583, 96, 732, 704, 759, 410, 690, 559, 531, 586, 288, 568, 437, 409, 464, 465, 745, 614, 586, 641, 343, 623, 492, 464, 519, 200, 480, 349, 321, 376, 78, 358, 227, 199, 254, 736, 249, 118, 90, 145, 614, 127, 763, 735, 23, 441, 721, 590, 562, 617, 319, 599, 468, 440, 495]



763
'''