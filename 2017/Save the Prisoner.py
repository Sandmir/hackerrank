__author__ = 'Senyutina'
t = int(input().strip())
for a0 in range(t):
    n, c, s = input().strip().split(' ')
    n, c, s = [int(n), int(c), int(s)]
    if n <c:
        ost = c%n
        print('ost ',ost)
        print('os dl ',(n-s+1))
        if ost <= (n-s+1):
            rez = s + ost -1
        else:
            rez = ost - n + s -1
            print('****')
    elif n == c:
        rez = c
    else:
        rez = -(c - (n - s))
        print('----')

    print(rez)

'''
100
987208066 992914997 534359308
829184434 845745270 142961264
64404787 990499813 50168775             ======== 540066238
973232645 986655633 434408426
650191283 693567669 248488463
387963979 393752728 124575669
386466373 819226471 169682152
567500739 588381573 190420213
110961316 653458893 101526651
586150889 857180048 295453561
127704787 193861372 30977470
501788512 623729607 40210994
155634995 840192364 67379577
205803769 275201320 38320173
465961192 558381223 172699145
14832220 415810197 10318522
543780156 962564973 467116054
498310524 705771963 14814365
108747827 279686934 76826909
987003690 989591835 514794082
307275380 659137273 292765922
126119867 343855730 30079437
520635724 620403066 35568703
988730256 998280807 119051985
85370549 942273400 35425691
121914462 882709797 34116370
16763475 68704330 10863644
423956193 809960449 369196359
284529005 779281087 255606461
687599395 919752746 149741813
41913518 872858186 944637
334679439 771705685 161826417
100114296 240933740 29923974
697590171 710271067 89040101
657888763 725325362 544794877
778685002 820552414 573284626
300459219 960008544 239663360
462194138 721685845 163473478
831390496 966320275 289029203
224042313 236306846 6607196
373784125 801746300 96239325
113353423 354727264 50251925
944538718 953259162 115648701
875491355 922431341 235809478
964531455 981986700 125165878
677620209 716269467 63235573
882106188 891674932 243031063
121769547 308646770 98937299
747437163 859305117 172137684
720373213 893899779 238530117
175065034 252652799 60775844
271304358 462245545 13431713
987727403 994128383 181105520
844969891 933306956 215457691
684278431 733370709 241354140
591023570 801695546 199572206
539636121 711686526 192467527
399395912 466459974 268802426
594259133 785796889 547355579
113787494 501178282 23584231
645580389 790357766 328746984
231551334 917827865 56585504
58896120 791796173 6076716
80245394 451735569 50190463
140672975 337114555 66996630
603100329 662293819 56178774
246212456 285157103 207673947
517952224 956292782 274738009
438062826 784850994 336987929
985418404 992773412 329146373
236577622 354216790 235558841
565324606 859200821 430395078
85012777 724976857 64092363
592697204 683695493 328405538
963869242 979122416 420304902
868093049 981852921 15389621
130472480 676172895 9119957
190662778 976359289 26128429
465400787 619961697 315082344
407156371 468850462 97303806
736302744 979785432 269182242
480421290 676955249 322855691
910816367 940172733 52003404
867731729 966587082 535545596
196137266 651136392 101460748
432827761 648989516 404820706
316310431 398943687 221910085
91254099 139493801 46359641
452021974 778452311 400192715
550422243 581653974 461886806
647726048 713813950 464706422
242030129 382843401 86757411
564885819 634028604 417543518
527705589 585258767 25873512
63251184 852487223 47757877
17228284 28557251 5346379
287704511 903048419 110994298
825925026 852218730 529759386
2358404 725790225 893285
402551118 481507417 312646264


540066238
159522099
10191995
447831413
291864848
130364417
215975876
211301046
89217647
566482719
97134054
162152088
129396965
107717723
265119175
10826558
342120714
222275803
30270361
517382226
30077054
121695432
135336044
128602535
38623051
63424932
12514073
331244421
181300532
381895163
35532462
264173223
70629121
101720996
612231475
615152037
298294246
422965184
423958981
18871728
150417374
64918919
124369144
282749463
142621122
101884830
252599806
42275427
284005637
412056682
138363608
204372899
187506499
303794755
290446417
410244181
364517931
335866487
144634201
69612536
473524360
48208032
32223328
20453667
122765234
115372263
406137
195126342
245713270
336501380
116620386
158946686
23954226
419403826
435558075
129149492
32930451
49173827
4242466
158997896
512664929
38968359
81359769
634400948
164185341
188154699
304543340
3345243
274601077
493118536
530794323
227570682
486686302
83426689
14728523
16675345
150929183
556053089
295077
391602562



100
352926151 380324688 94730870
94431605 679262176 5284458
208526924 756265725 150817879
962975336 972576181 396355184
464237185 937820284 255816794
649320641 742902564 647542323
174512033 711706897 68977959
107283902 156676511 67149447
104513201 298399273 96292548
113378824 274011418 98103763
934815799 991959468 212396037
88325121 435452998 24617705
984873585 997634055 103050157
344218387 715364875 90658180
556065259 615709967 156417592
57109959 451440582 4188603
353972922 573651462 244520504
946486979 973168361 647886035
368127406 680428368 105517295
884634320 965112925 119757238
422557970 744431033 28932300
634954007 957414623 341366379
190265362 445253893 184632922
293315518 479153471 120684020
72410472 80198999 984948
784893322 849791807 360911386
846191883 880790237 510053756
297201660 812278057 198376746
945087694 999220046 465061514
786859800 831171414 378370933
528402029 859318899 224559950
522640531 755821672 28838424
864006909 879474138 806467486
613544440 943850900 258190755
734228459 928771704 265979283
542812502 597832172 330877768
541133561 748691081 126348492
51187317 524866691 1143193
885290374 990676850 373368385
147955933 450823700 138416059
100046465 587967212 32555061
233926824 996957988 31809378
785405778 835771758 689182705
444389615 870657324 72775880
702580369 895325888 345053199
968559651 974760313 326732084
299437419 514618345 254272806
901702945 930227426 727030891
721843209 736359383 225283784
833018320 883439261 806599246
267346244 307857609 46989880
299901304 892163356 210218436
565637506 795821687 158300457
107336562 781910357 54488503
513281286 916998022 254269425
413431205 611661371 188998419
740163288 938647312 571382392
44702121 296589002 43470596
771733011 919327188 317638907
718860003 815844769 495144331
377975600 438513404 111085209
424965480 928959619 20776133
234986523 732169039 205952749
377078343 981597420 219264561
612269027 791414524 580170106
232336090 616084008 81392003
75059328 274029861 53524881
239121359 646856043 141349731
923193147 943368157 206717532
12565064 536852817 11557940
360225746 970375527 284883902
213705306 380885426 14495860
659446919 699401237 73837176
335372713 785363124 7610828
538388654 859196325 110284314
118558760 713483972 83950807
896959032 961368580 8848444
25543240 521123082 2472730
258530682 935834352 194732411
465248213 679599042 334563499
331230504 637771661 76778140
976340152 988657462 243958260
552994811 922743535 540135280
626831986 839281366 24222267
157704591 253731033 59023773
806377559 859228114 238044289
838798445 996851254 268459446
847646888 928001503 755190846
877625009 999275937 874127074
847949466 893343194 10497830
35029316 784675240 8200127
111807455 690309882 23190325
355765714 554560093 311565654
1890615 614626804 976253
132293206 165429783 65360680
506726160 934170235 455394293
210041918 328800789 159203369
499999999 999999997 2
499999999 999999998 2
999999999 999999999 1

122129406
23525398
72975907
405956028
265162707
91803604
82636723
9258153
81152217
31978708
269539705
18445097
115810626
117586280
216062299
55859471
110226121
674567416
49690850
200235842
350805362
28872987
59090728
13206454
8773474
425809870
544652109
119049822
519193865
422682546
27074790
262019564
821934714
588497214
460522527
385897437
333906011
14136713
478754860
145371959
20243482
93060069
739548684
54653973
537798717
332932745
170016312
755555371
239799957
24001866
87501244
202677879
388484637
85042925
144704874
387228584
29703127
27144750
465233083
592129096
171623012
99804791
233162218
69626951
147046575
467740
27317429
70841696
226892541
8113004
174582190
181675979
113791493
122228525
431091984
86082218
73257991
12731011
96444034
83666114
52088792
256275569
356889192
236671646
155050214
290894843
426512254
835545460
118152992
55891557
22230414
42655476
154594318
1153181
98497256
376112207
67920321
499999999
1
999999999

'''