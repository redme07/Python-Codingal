def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

text = input("Enter a sentence: ")
print("Reversed sentence:", reverse_words(text))






