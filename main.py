from functions import *

print '''
Hello student. This is a text editing program. /n
You can change words, find the word count, /n
change sentences, and find sentence lengths. '''

print '''
Input which of the following programs you would like to use:
change words, word count, change sentence, or sentence lengths.
'''

program_choice = raw_input("> ")

def check_program_choice():
        if program_choice == "change words":
                print "Now input the text that you would like to edit."
                        text = raw_input("> ")
                print "Next, input the word you would like to change."
                        word = raw_input("> ")
                print "Finally, input the word you like to replaace it with."
                        replacement = raw_input("> ")

                return change_word(text, word, replacement)

        elif program_choice == "word count":
                print "Now input the text that you would like to edit."
                        text = raw_input("> ")
        
                print word_count(text)

        elif program_choice == "sentence lengths":
                print "Now input the text that you would like to edit."
                        text = raw_input("> ")

                print sentence_lengths(text)

        elif program_choice == "change sentence":
                print "Now input the text that you would like to edit."
                        text = raw_input("> ")
                print "Next, input the sentence you would like to change."
                        sentence = raw_input("> ")
                print "Finally, input the sentence you like to replaace it with."
                        replacement = raw_input("> ")

                return change_sentence(text, sentence, replacement)

        else:
                print '''
                I'm sorry. That was not one of the program choices. 
                Restart program to try again.
                '''
        

             