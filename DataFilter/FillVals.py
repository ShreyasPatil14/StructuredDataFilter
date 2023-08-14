# Processing Funcs:- [Phase-2]
# (dealing with missing values)

import pandas as pd
from sklearn.linear_model import LinearRegression
import Global


# getting coefficient of data
def regression(data):
    
    data = pd.DataFrame(data)
    
    # splitting data into x and y
    x = data.iloc[:,:-1]
    y = data.iloc[:,-1]

    # creating object of linear regression model
    model = LinearRegression()
    
    # applying regression
    model.fit(x, y)
    
    # getting y-intercept and other coefficient values
    coeff_list =   list (model.coef_)
    y_intr = round(model.intercept_, 2)
    
    # list to collect y_intr and thetas
    theta_list = []
    
    # collecting all theta values together
    theta_list.append( y_intr )
    for vals in coeff_list:
        theta_list.append(  round(vals, 2) )
     
    return theta_list

#   -    -     -    -    -   -   -    -    -    -    -   -     -    -    -    -    -    -    -    

# returning data with all missing values filled   
def fillMissVal(data, missValList, thetas, y_intr):
    
    for iteration in range( len(missValList) ): # itrating for all missing values
        
        row = missValList[iteration][0]  # row idx of missing value
        col = missValList[iteration][1]  # col idx of missing value
        value = data[row][len(data[0])-1]   # label value associated with missing value
        
        value = value - y_intr # subtracting x-coordinate value from label value
        
        for i in range( len(thetas) ): # iterating for all other values in record
            
            if( data[row][i] != None ): # subtract 
                value = value - data[row][i] * thetas[i]
            
        data[row][col] = round(value / thetas[col], 2)
    
    return data

#   -    -     -    -    -   -   -    -    -    -    -   -     -    -    -    -    -    -    -    

# operating on missing values [main function]
def setMissing(data, rows, cols):
    
    # getting complete data
    com_data = []
    com_row = []
    
    # getting missing values index
    missing_values_list = []
    miss_val_idx = []
    
    for row in range(rows):
        
        com_flag = True
        for col in range(cols):
            
            if( data[row][col] == None ):
                
                miss_val_idx.append(row)
                miss_val_idx.append(col)
                missing_values_list.append(miss_val_idx)
                miss_val_idx = []
                
                com_flag = False
                break
        
        if(com_flag):
            
            for col in range(cols):
                com_row.append(data[row][col])
                
            com_data.append(com_row)
            com_row = []
            
    # can`t process further if data got more than 30% missing values
    if( len(com_data) < rows*30/100 ):
        Global.exit_flag = True
        return 
    
            
    del(com_row)
    del(miss_val_idx)
    
    # getting y-intercept and theta values
    theta_list = regression(com_data)
    
    y_intr = theta_list[0]
    thetas = theta_list[1:]
    del(theta_list)
    del(com_data)
    
    # filling missed values
    return fillMissVal(data, missing_values_list, thetas , y_intr)