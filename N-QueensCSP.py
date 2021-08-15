
############################################################################################
#Constants!

N = 8 #Size we are choosing

QUEEN_SYMBOL = 2 #2 means queen, 0 means no queen

############################################################################################



#This is a list of all the queen's locations in each row. The value of 0 means nothing placed
queen_placed = [0 for i in range(0,N)]


#This function is meant to scan if there is a queen present in a given row.
def scanForQueen(queens_array,row):
    column = 0
    for column in range(0,N):
        if (queens_array[row][column] == QUEEN_SYMBOL):
            queen_placed[row] = column + 1  # there is a queen in the row



#diagonal constraint, make sure nothing is diagonal from the queens already placed.
def diagContraint(queens_array, new_row, new_column):

    i = 0
    queen_column = 0
    queen_row = 0
    #go through each row, if queen is present want to check if the new location is potentially diagonal from the queen we are looking at.
    for i in range(0,N):
        if(i == new_row):
            continue
        if(queen_placed[i] != 0):
            queen_row = i
            #this is the trick we had from before to save the queen's location and know if a queen is in the current row all at the same time.
            queen_column = queen_placed[i] - 1

            row_diff = abs(queen_row - new_row)
            col_diff = abs(queen_column - new_column)

            if(row_diff == col_diff):

                return False #constraint is not respected

    return True #all rows are safe


#constraint to ensure nothing is in the same column
def colConstraint(queens_array, new_column):
    i = 0

    for i in range(0,N):
        if(queens_array[i][new_column] != 0):
            return False

    return True

#constraint to ensure that no other queens are on the same row
def rowConstraint(queens_array, new_row):
    j = 0

    for j in range(0,N):
        if(queens_array[new_row][j] != 0):
            return False

    return True

#The meat of the solution, this is the function that finds the optimal placement of the queens to solve this Constraint Satisfaction Problem (CSP)
def backTrackingSearch(queens_array,row):
    #If the current row is N, we know we made it to the end,
    if row == N:
        return True, queens_array

    #If there is a queen in the current row, pass.
    if(queen_placed[row] == 0):
        col = 0
    
        #Go through every possible position in the row
        for col in range(0,N):

            queen_placed[row] = 0 

            #check if all 3 constraints are satisfied
            if((rowConstraint(queens_array,row) == True) and (colConstraint(queens_array,col) == True) and (diagContraint(queens_array,row,col) == True)):
                #Set the queen at this row at the current position, saving it in 2 places 
                queen_placed[row] = col + 1
                queens_array[row][col] = QUEEN_SYMBOL

                #Recursively go down to the next level in hopes of having found the "right" conbination
                ret = backTrackingSearch(queens_array,row +1)

                #If it returns true, we know that we made it to the end and as such can break out
                if ret[0] == True:
                    return ret

            #Reset changes made and try again with another position if we didnt find a good path.
            queens_array[row][col] = 0
            queen_placed[row] = 0 
    else:
        #if the queen was already placed on this row, move on the the next one.
        ret = backTrackingSearch(queens_array,row +1)

        #If it returns true, we know that we made it to the end and as such can break out
        if ret[0] == True:
            return ret
    

    return False,queens_array

#function that prints the board nicely 
def printBoard(queens_array):
    for line in queens_array:
        print(line)      







#This is the function that runs things and calls the algo.
def main():
    
    #variables used for iteration
    i = 0
    j = 0



    #generate the queens array (the board we are playing on)
    queens_array = [[0 for i in range(0,N)] for j in range(0,N)]
    # queens_array = [[0,0,0,0,0,0,0,0], 
    #                 [0,0,0,0,0,0,0,0],
    #                 [0,0,0,0,0,0,0,0],
    #                 [0,0,0,0,0,0,0,0],
    #                 [0,0,0,0,0,0,0,0], 
    #                 [0,0,0,0,0,0,0,0],
    #                 [0,0,0,0,0,0,0,0],
    #                 [0,0,0,0,0,0,0,0]] 



    #we can place a queen wherever we want, this is only to be used when the prof selects the location for the queen. You can get rid of this and it'll work.
    queens_array[3][2] = QUEEN_SYMBOL

    #have it scan over the array and just save the position of the queen, wherever it is just so we can access it easier 
    for i in range(0,N):
        scanForQueen(queens_array,i)


 
    #start the algorithm at the beginning of the board (0th row)
    ret = backTrackingSearch(queens_array,0)

  
    #get the returned "solved" board
    queens_array = ret[1]

    #this is my function to print it out
    printBoard(queens_array)



main()

