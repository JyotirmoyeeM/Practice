#write a program to find shortest word in a sentence
def shortest_word(sentence):
    word = sentence.split()
    shortest = word[0]
    for i in word[1:]:
        if len[i] < len[shortest]:
            shortest = i
    return shortest
