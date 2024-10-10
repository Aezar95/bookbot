from collections import Counter

def count_words(text):
    """Counts the number of words in the text."""
    words = text.split()
    return len(words)

def count_characters(text):
    """Counts the occurrences of each character in the text."""
    # Convert the text to lowercase
    text = text.lower()
    # Use a Counter to count occurrences of each character
    character_count = Counter(text)
    return character_count

def generate_report(file_path):
    """Generates a word and character count report for the given text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Count the number of words
    word_count = count_words(text)
    
    # Count the occurrences of each character
    char_count = count_characters(text)
    
    # Filter to include only alphabetic characters
    char_count = {char: count for char, count in char_count.items() if char.isalpha()}
    
    # Sort the characters by their count in descending order
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    
    # Print the report
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

# Example usage
file_path = 'books/frankenstein.txt'  # Replace with your actual file path
generate_report(file_path)