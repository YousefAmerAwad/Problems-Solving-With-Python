#function that add commas to the number
def add_commas(number):
    number = str(number)    #convert the int number to string
    num_list = []    #initialize an empty list 
    for n in number:
        num_list.append(n)  #fill the empty list with the number

    numOf_commas = int((num_list.__len__() - 1)/3)  #calculate number of commas
    index = -3  #first index in which we should add our commas
    for __ in range(numOf_commas):
        num_list.insert(index,',')  #add comma to the list containing our number
        index -= 4  #the new index
    
    num_new = ''.join(num_list) #convert the list to string
    return num_new 