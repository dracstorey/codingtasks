# Original lists
list1=[2,5,15,36,47,56,59,70,156,244,268]
list2=[18,39,42,43,67,69,100]

# New list to hold the merged values
MergeList=[]

# Current poiinter to place in list 1
index1=0

# Current pointer to place in list 2
index2=0

# Loop until one of the lists comes to an end
while index1 < len(list1) and index2 < len(list2):
    
    # If list1 value is smaller than current list2 value append list1 value to mergelist
    if list1[index1] < list2[index2]:
        MergeList.append(list1[index1])
        #increase list1 pointer
        index1 = index1 + 1
    else:
        # append list2 value to mergelist nas that is smaller
        MergeList.append(list2[index2])
        # increase list2 pointer
        index2 = index2 + 1
    # end if

# end while

# Loop round any remianin values of list1 and add them to mergelist
for i in range (index1,len(list1)):
    MergeList.append(list1[index1])
# end for

# loop round any remaining values of list2
for j in range (index1,len(list1)):
    MergeList.append(list1[index1])
# end for

print (list1)
print (list2)
print (MergeList)

