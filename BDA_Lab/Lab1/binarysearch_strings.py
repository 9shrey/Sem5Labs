def binary_search_word(sentence, word):
    words = sentence.split()
    words.sort()
    low = 0
    high = len(words) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_word = words[mid]
        
        if mid_word == word:
            return mid
        elif mid_word < word:
            low = mid + 1
        else:
            high = mid - 1

    return -1

sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")

index = binary_search_word(sentence, word)

if index != -1:
    print(f"Word '{word}' found at index {index}")
else:
    print(f"Word '{word}' not found in the sentence")
