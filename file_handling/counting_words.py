from collections import Counter
from string import punctuation

with open(
    r"C:\Users\amaab\OneDrive\Desktop\Python\file_handling\word.txt",
    encoding="utf-8",
) as file:
    file_data = file.read()

words = file_data.split()

word_count = len(words)
comma_count = file_data.count(",")
punctuation_count = sum(char in punctuation for char in file_data)

total_len_of_words = sum(map(len, words))

top_words = Counter(words).most_common(3)

print(words)
print(word_count)
print(comma_count)
print(top_words)
print(punctuation_count)

average_word_length = total_len_of_words / word_count if word_count else 0

print(average_word_length)
