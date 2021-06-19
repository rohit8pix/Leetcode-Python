# O(N2) Solution
#can be reduce to O(N) using Depth First Search (DFS)
def spiralOrder(matrix):
    row_end=len(matrix)
    col_end = len(matrix[0])
    row_beg=0
    col_beg=0
    ans=[]
    size=len(ans)

    num=(row_end*col_end)
    while size<row_end*col_end:

        #going right till the end of last column
        # update the value of row by incrementing it by one
        # as next interation will run through next row 
        # DIRECTION RIGHT

        for i in range(col_beg,col_end):        
            ans.append(matrix[row_beg][i])                                    
            #print(row_beg,i,"right")            
        row_beg+=1

        #going down till last row
        #then updating the col by decrementing by 1
        #DIRECTION DOWN

        for j in range(row_beg, row_end):
            ans.append(matrix[j][col_end-1])
            #print(j,col_end-1,"down")
        col_end-=1

        #going left till col_beg
        #updating the value of row by decrementing it
        #DIRECTION LEFT

        for k in range(col_end-1,col_beg-1,-1):
            ans.append(matrix[row_end-1][k])
            #print(row_end-1,k,"left")
        row_end-=1

        #going up till row_beg
        #DIRECTION UP

        for h in range(row_end-1,row_beg-1,-1):
            ans.append(matrix[h][col_beg])
            #print(h,col_beg,"up")
        col_beg+=1

    return(ans[:num]) # printing element only till the size of mxn
