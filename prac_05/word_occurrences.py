from operator import itemgetter

# Function to count word occurrences
def count_words(text):
    words = text.split()
    word_count = {}

    # Count occurrences of each word
    for word in words:
        word = word.lower()  # Consider case insensitivity
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Main program
def main():
    text = input("Text: ")
    word_count = count_words(text)

    # Sort the dictionary by values (word counts)
    sorted_word_count = sorted(word_count.items(), key=itemgetter(1), reverse=True)

    # Calculate the maximum width for words and counts
    word_width = max(len(word) for word, _ in sorted_word_count)
    count_width = max(len(str(count)) for _, count in sorted_word_count)

    # Print the word counts aligned
    print("\nWord Counts:")
    for word, count in sorted_word_count:
        print(f"{word:<{word_width}} : {count:{count_width}}")

# Run the program
if __name__ == "__main__":
    main()