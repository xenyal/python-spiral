def spiral(rows, cols):
    m = [[0 for i in range(cols)] for j in range (rows)]
    x = 0
    y = -1
    counter = 0
    col_counter = cols
    rows_counter = rows - 1
    while counter <= cols*rows:
        if counter == cols*rows:
            return m
        for i in range (0, col_counter):
            y+=1
            counter += 1
            m[x][y] = counter
        col_counter -= 1
        if counter == cols* rows:
            return m        
        for i in range (0, rows_counter):
            x+=1
            counter += 1
            m[x][y] = counter
        rows_counter -= 1      
        if counter == cols* rows:
            return m        
        for i in range (0, col_counter):
            y-=1
            counter += 1
            m[x][y] = counter
        col_counter -= 1
        if counter == cols* rows:
            return m        
        for i in range (0, rows_counter):
            x-=1
            counter += 1
            m[x][y] = counter
        rows_counter -= 1      
    
print spiral (5,4)    

