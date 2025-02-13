def speak_up(sentence):
    sentence.pop()
    sentence.append('!')

    return sentence


words = ['Программировать', 'круто', '.']

more_words = {'Пиши', 'код', '.'}

print(speak_up(words))  

print(speak_up(more_words))