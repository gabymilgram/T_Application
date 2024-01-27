

def boxed_strings(string_list):
    longest = max(string_list, key = len) # determine longest word
    print('*' * (len(longest)+4)) # print top line of border
    for word in string_list:
        print("* " + word + " " * (len(longest) - len(word)+1) + "*") # format words
    print('*' * (len(longest)+4)) # print bottom line of border



