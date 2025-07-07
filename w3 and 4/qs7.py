#this function displays the frequency of each word in the sentence
def word_frequency(sentence):
    word_counts = {}
    words = []
    current_word = []
    for char in sentence.lower():
        if char.isalpha() or char == "'":
            current_word.append(char)
        elif current_word:
            words.append(''.join(current_word))
            current_word = []
    if current_word: 
        words.append(''.join(current_word))
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts

def test_word_frequency():
    test_cases = [
        ("Hello world hello", {'hello': 2, 'world': 1}),
        ("Python TEST test", {'python': 1, 'test': 2})
    ]
    
    for i, (sentence, expected) in enumerate(test_cases, 1):
        result = word_frequency(sentence)
        print(f"\nTest Case {i}: '{sentence}'")
        print("Expected:", expected)
        print("Result:", result)
        print("Status:", "PASS" if result == expected else "FAIL")

if __name__ == "__main__":
    print("WORD FREQUENCY TESTING")
    test_word_frequency()
