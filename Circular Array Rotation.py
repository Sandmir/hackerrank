__author__ = 'Senyutina'

n, k, q = map(int, input().strip().split())

arr = [int(a_temp) for a_temp in input().strip().split(' ')]
m = []
for i in range(q):
    m.append(int(input()))
k %= n
arr1 = arr[-k:] + arr[:-k]

for i in m:
    print(arr1[i])




'''
n, k, m = map(int, input().strip().split())
exs = '29261 80254 86934 3704 76338 96698 47885 88475 65211 65976 75238 58566 28684 20348 45383 58620 48360 99801 51885 82661 83066 14311 24803 99267 21541 93195 21194 20775 64817 42323 7640 10429 38928 94573 30484 15265 7622 78368 3739 72833 60696 95328 31398 5731 15676 93132 64351 64035 9284 32587 46695 92349 46897 87850 7968 84789 81044 45513 5563 62212 87836 13202 88993 26763 24127 19476 42028 31748 14196 62118 4580 91243 73798 52329 96973 89473 61812 77675 69859 71095 10261 32905 79796 57157 20754 87763 41945 1798 33275 63859 80361 37462 93413 69353 64225 17539 5181 22604 49286 19376 1073 70218 26970 74870 38898 23942 80694 710 1617 50552 88156 11877 83457 67951 85386 4210 55713 43682 22359 5340 23893 2720 59153 17305 88424 23377 51195 93604 62332 480 29331 79757 87049 56300 54626 25947 96594 35320 26656 98210 2223 31163 26438 85679 99114 28175 89889 71178 88209 12247 76517 12101 31318 35670 45757 19742 75398 96951 29697 54082 13782 75380 33838 831 31679 4815 26777 28272 56486 69784 42833 58709 946 85623 44387 59 13797 50627 87589 2005 62874 80457 14105 94191 32478 59861 30284 7876 73163 59981 78309 86945 35360 28498 87775 83390 49664 30903 28014 6150 686 70846 81210 17983 56468 41948 34394 86617 92575 21982 88621 71800 2438 19078 82342 34916 95290 12626 59143 68453 88958 37451 71749 24317 82300 59523 24058 31963 90425 52071 54464 7462 39269 35673 25444 12088 93973 76189 98704 86547 98170 3677 74698 16960 22754 57039 51875 34395 86016 11017 19199 74973 64819 90947 15641 63470 66821 39699 95432 73597 91769 49896 81058 31037 1920 22854 43125 12244 99042 58180 15142 13564 61856 89839 30523 961 63230 98749 51708 49245 26117 70906 24218 90935 78205 39858 54404 45025 95908 66187 34974 87677 32434 32383 35065 50706 55236 78189 62949 70630 36369 78091 545 14576 67929 47419 15537 31158 46167 67244 96755 72283 54501 37324 79569 32705 77181 50324 94082 73089 16510 45407 77117 65296 77789 12181 16001 49377 6722 78949 36358 59442 73391 36902 74017 41320 84320 5905 88829 46838 89500 1935 19120 44001 39258 98688 93057 32791 49011 3490 22231 81872 48896 99347 47167 26685 27879 79519 92413 34600 74820 28770 94041 48210 65671 84410 5881 66342 90314 11062 13179 96166 12996 32298 40166 52254 47337 49574 85044 12699 53064 7274 94570 18311 22972 58089 61347 50850 37607 53759 1802 12426 82528 12194 60636 64550 96603 66516 30891 3269 93929 60421 99434 6925 9070 55951 59178 56406 5524 60573 69104 74939 84198 80026 93250 7169 38114 54596 74370 92072 24707 76171 4498 7234 88365 81485 71784 84967 64352 19026 4587 58281 79447 20372 65205 88516 92674 40734 44922 98198 17658 30377 89488 1855 10402 99089 25375 64867 70037 99744 56939 94743 75915 77788 1976 64279 75624 90111 65597 39975 9137 70184 98255 88583 6907 79811 93450 99581 36896 38371 14130 54553 85100 3617 72759 11853 19058 98133 76720 89094 97877 50010 188 73791 44149 18515 54421 19772 8626 20017 59746 17762 6552 74353 22696 13459 70515 16145 29391 7411 70868 43520 78315 55967 63488 51074 84171 82545 49206 60890 87990 63434 27251 4529 53576'
arr = [int(a_temp) for a_temp in exs.split(' ')]
k %= n
arr = arr[-k:] + arr[:-k]
for i in range(m):
    print(arr[int(input().strip())])
'''