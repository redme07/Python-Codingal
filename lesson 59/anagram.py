str1 = input('enter a word: ')
str2 = input('enter another word: ')

def frequency(str):
    freq = {}
    str = str.replace(" ","").lower()
    for i in range(len(str)):
        if str[i] in freq.keys():
            freq[str[i]]+=1
        else:
            freq[str[i]]=1
    return freq

def anagram(str1,str2):
    if frequency(str1) == frequency(str2):
        return "the two words are anagrams"
    else:
        return "the two words are not anagrams"
print(anagram(str1,str2))
