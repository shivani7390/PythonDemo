lst=[[1,2,0,'a','b','c'],3,4,5,'d','e','f',[6,7,'g','h'],[8,9],'i','j']
for i in range(len(lst)):
    if type(lst[i])==list:
        for j in range(len(lst[i])):
            if type(lst[i][j])==int:
                print(lst[i][j])
            else:
                print(" ",lst[i][j])
    elif type(lst[i])==int:
        print(lst[i])
    else:
        print(" ",lst[i])
