import bisect

#bisect, bisect.bisect_left, bisect_right

a=[1,2,2,2,3]

bisect.bisect_left(a,2) #1
bisect.bisect_right(a,2) #4
bisect.bisect(a,2) #4



#bisect.insort
a=[10,20,30,40,50,60,70,80,90,100]

bisect.insort(a,55)
# [10, 20, 30, 40, 50, 55, 60, 70, 80, 90, 100]


