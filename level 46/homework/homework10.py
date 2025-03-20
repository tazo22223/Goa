sentence = "The quick brown fox jumps over the lazy dog"
vowels = "aeiou"

words = sentence.split()
filtered_words = [word for word in words if any(vowel in word.lower() for vowel in vowels) and len(word) >
