#Using list slicing
main_list= [1,2,3,4,5,6]
rever_list=[]
print(main_list)
print("Reverse list",main_list[::-1])

#Reverse list with for loop
for i in main_list:
     rever_list.insert(0,i)
print(main_list)
print(rever_list)
