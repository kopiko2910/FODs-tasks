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
        ("The quick brown fox jumps over the lazy dog", 
         {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}),
        ("", {}),
        ("Don't stop believing", {"don't": 1, 'stop': 1, 'believing': 1}),
        ("Python! is, awesome. Python?", {'python': 2, 'is': 1, 'awesome': 1}),
        ("Multiple   spaces   here", {'multiple': 1, 'spaces': 1, 'here': 1}),
        ("Case TEST test TeSt", {'case': 1, 'test': 3})
    ]
    
    for i, (sentence, expected) in enumerate(test_cases, 1):
        result = word_frequency(sentence)
        print(f"\nTest Case {i}: '{sentence}'")
        print("Expected:", expected)
        print("Result:", result)
        print("Status:", "PASS" if result == expected else "FAIL")

if __name__ == "__main__":
    print("WORD FREQUENCY TESTING")
    print("----------------------")
    test_word_frequency()
