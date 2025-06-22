"""Start

Prompt user: "Text: "
Read text_input

Convert text_input to lowercase
Split text_input into a list of words and store in words_list

Create an empty dictionary called word_to_count

FOR EACH word IN words_list
    IF word IN word_to_count THEN
        Increment word_to_count[word] by 1
    ELSE
        Set word_to_count[word] to 1
    END IF
END FOR

Set max_word_length to 0

FOR EACH word IN word_to_count
    IF length of word > max_word_length THEN
        Set max_word_length to length of word
    END IF
END FOR

FOR EACH word IN word_to_count sorted alphabetically
    Display word, formatted with width of max_word_length, followed by " : " and word_to_count[word]
END FOR

End
"""

"""
Word Occurrence Counter
Estimated time: 15 minutes
Actual time: [Record your actual time after completing]
"""

# Prompt the user to enter a string
text = input("Text: ")

# Convert the input to lowercase to make counting case-insensitive
words = text.lower().split()

# Count word occurrences using a dictionary
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

# Find the length of the longest word for formatting
max_word_length = max(len(word) for word in word_to_count)

# Print the results sorted alphabetically by word
for word in sorted(word_to_count):
    print(f"{word:{max_word_length}} : {word_to_count[word]}")
