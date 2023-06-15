def count_word_frequency(file_path):
    word_frequency = {}
    
    # Open the file
    with open(file_path, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into words
            words = line.strip().split()
            
            # Count the frequency of each word
            for word in words:
                if word in word_frequency:
                    word_frequency[word] += 1
                else:
                    word_frequency[word] = 1
    
    return word_frequency

def main():
    file_path = input("Enter the path to the text file: ")
    
    # Count word frequency
    word_frequency = count_word_frequency(file_path)
    
    # Display word frequency
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
