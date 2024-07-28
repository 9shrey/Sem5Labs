from collections import Counter
with open('data.txt', 'r') as file:
    data = file.read().split()
    word_counts = Counter(data)
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
for word, frequency in sorted_words:
    print(f"Word: '{word}' - Frequency: {frequency}")
