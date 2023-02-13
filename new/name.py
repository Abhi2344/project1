procedure bubblesort (list:[5,3,4,1])

loop=list.count();
for i=0 to i=loop-1:
    swap=False

    for j=0 to j=loop-1:
        
        if list[j]>list[j+1] then
        swap(list[j],list[j+1])
        swap is true

        end if   
    end for
     
    if(not swap) then
       break
    end if
 end for
 end procedure return list