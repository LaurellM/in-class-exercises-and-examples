# Warm Up - fix this function.

# This function is supposed to take a list of words and return a new 
# list with the one-letter words removed. It's not doing that. First,
# run the function with some test word lists to see what it is doing
# then fix it so it has the desired output.

def remove_short_words(word_list):
    new_list = []
    for word in word_list:
        if len(word) > 1:
            new_list.append(word)
    print(new_list)
    
    
test_list = ["a", "words", "are", "a", "I", "simple", "cat", "I"] 

remove_short_words(test_list)
