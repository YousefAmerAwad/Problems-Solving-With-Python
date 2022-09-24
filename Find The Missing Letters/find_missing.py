import string


letters = string.ascii_lowercase    #all english letters

def find_missing(string):
    first_position = letters.find(string[0])    #firsh position of the right letters
    last_position = letters.find(string[-1])    #firsh position of the right letters
    right_string = letters[first_position:last_position+1]  #right letters

    missings = []   #initialize the list of missing letters
    for char in right_string:   
        if char in string:  #if char is one of the input letters, don't append it in missings list
            continue
        else:
            missings.append(char)   #if char is not exist in input letters, append it in missings list

    if missings.__len__() == 0: #if missings list is empty, then there is no missing letters
        print('There is no missing letters')
    else:
        print(f'The missing letters are {missings}')   #if missings list is not empty, then print the missing letters


    



input = input('Write your letters: ')   #take input from user
find_missing(input)