str = input('enter a word: ')

def frequency(str):
    freq = {}
    str = str.lower()
    for i in range(len(str)):
        if str[i] in freq.keys():
            freq[str[i]]+=1
        else:
            freq[str[i]]=1
    return freq

print(frequency(str))