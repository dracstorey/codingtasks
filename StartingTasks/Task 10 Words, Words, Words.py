
## Task 10. Print how manyb words are in a sentence.
## User inpyts a sentence
sentence = input("Input a sentence") 

# Test sentence
#sentence = "Hello Dr Kinch how   are you   today.  "

# Flag to record if the character is a space or not. Setbto Tru so first character can be counted
s_flag = True

# Number of words counted (final output)
words = 0

# Loop counter
counter = 0

# Iterate through each letter of the sentence
while counter < len(sentence):
    # If we encounter a space set space flag to true
    if sentence[counter] == " ":
        s_flag = True
    else:
        # If space flag is true and character is not a space then new word begins
        if s_flag == True:
            # Increae number of words by 1
            words = words + 1
            # set spave flag to false so we don't count anorther word if next character is a letter
            s_flag = False
    # increment the loop counter
    counter = counter + 1


print("There are", words, " words in this sentence")