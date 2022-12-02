#Loops
l =[x for x in range(0,10)]
for x in l:
    print(x, end=", ")
l =[x for x in range(0,10)]
#for break it is stopped at 3
for x in l:
    if(x==4):break
    print(x)
l =[x for x in range(0,10)]
#for continue 4 is skipped
for x in l:
    if(x==4):continue
    print(x)
#while loop
a= 10
while a != 0:
    print(a)
    a-=1

nums = [x for x in range(0,11)]
index = 0
while index < len(nums):
    print(nums[index])
    index +=1

