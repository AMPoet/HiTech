#HiTech

my_set={1,2,3,4,5,6,7,7,6,2,4,5}  #Define a Set
print(my_set)                     #output: {1,2,3,4,5,6,7}

############################

my_set=set([1,2,3,4,5,6,7])
print(my_set)                      #output: {1,2,3,4,5,6,7}

############################

print( 7 in my_set)                #output: True
print(9 in my_set)

############################

my_set.add(88) 
print(my_set)                      #output: {1, 2, 3, 4, 5, 6, 7, 88}

############################

my_set.remove(3)           
print(my_set)                      #output: {1, 2, 4, 5, 6, 7}
print(3 in my_set)                  #output: False

############################

my_set.discard(7)                   #output: {1, 2, 4, 5, 6}
print(my_set)

############################

my_set={1,2,3,4,5,6,7}
my_set2={4,5,6,7,8,9,10}

intersection_set=my_set.intersection(my_set2)

print(intersection_set)           #output:{4, 5, 6, 7}

############################


union_set=my_set.union(my_set2)
print(union_set)                  #output:{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

############################

difference=my_set2.difference(my_set)

print(difference)                #output:{8, 9, 10}


#Telegram: https://t.me/HiTech_Codes

#Youtube:https://www.youtube.com/channel/UCBc3aSf54eyrl46RUWqIOIg?sub_confirmation=1