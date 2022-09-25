

def find_longest(string):
    longest = ''    #initialize longest word
    words = string.split(' ')   #list of all words is the string

    #find the longest word
    for word in words:
        if word.__len__() > longest.__len__():  
            longest = str(word)
    
    #if there is multible words that have the same max number of letters, list them all in longest_list
    longest_list = []   #initialize
    for word in words:
        if word.__len__() == longest.__len__(): 
            longest_list.append(word)

  
    return longest_list


input_str = str(input('Write a string: '))   #take input from user
print(f'longst words are {find_longest(input_str)}')
