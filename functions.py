def splitting_by_word(text):
    newList= list()
    newString = str()
    for i in range(len(text)):
        if text[i] == (" "):
            newList.append(newString)
            newString = ("")
        elif text[i] == ("."):
            newList.append(newString)
            newString = ("")
        else:
            newString += text[i]
    return newList

#print splitting_by_word("Hello, my name is Alex.")

def splitting_by_sentence(text):
        newList= list()
        newString = str()
        for i in range(len(text)):
                if text[i] == ("?"):
                        newList.append(newString)
                        newString = ("")
                elif text[i] == ("."):
                        newList.append(newString)
                        newString = ("")
                elif text[i] == ("!"):
                        newList.append(newString)
                        newString = ("")
                else:
                        newString += text[i]
        return newList

def change_word(text, word, replacement):
    newString = str()
    for item in splitting_by_word(text):
        if item == word:
            newString += replacement
        else:
            newString += item
        newString += " "
    return newString

#print change_word("The turtle walks by the dog.", "turtle", "cat")

def word_count(text):
    counter = 0
    for i in range(len(text)):
        if text[i] == (" "):
                counter += 1
    counter +=1 #accounts for last word
    return counter

print word_count("This is a test. There should be 9 words.")

def sentence_lengths(text):
        newList= list()
        newString = str()
        counter = 0
        for i in range(len(text)):
                if text[i] == (" "):
                        counter += 1
                elif text[i] == ("."):
                        newString = (counter)
                        newList.append(newString)
                        counter = 0
        return newList
#print sentence_lengths("The cat jumped over the dog. The dog was mad.")

def change_sentence(text, sentence, replacement):
    newString = str()
    for item in splitting_by_sentence(text):
        if item == sentence:
            newString += replacement
        else:
            newString += item
        newString += " "
    return newString

#print change_sentence("Hello my name is Alex. I have 2 cats.", " I have 2 cats", "I have 1 cat.")