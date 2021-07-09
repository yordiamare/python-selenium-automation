#Reverse a Statement
#Build an algorithm that will print the given statement in reverse.

#def reverse_statement(s):
    #word_list = s.split()
   # word_list.reverse()
  #  reversed_sentence = " ".join(word_list)
 #   return reversed_sentence

#print(reverse_statement("Everything is hard before it is easy"))

#str = "Everything is hard before it is easy"
#print(str)
#print (reverse_statement(str))


#Count Characters
#Create a program that will count vowels and consonants in a string.
#Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}
def count_characters(s):
    vowels = 0
    consonants = 0
    for i in s:
        if i == '':
            continue
        if (i == 'a'or i == 'e'or i == 'i'or i == 'o' or i == 'u' or
            i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U'):
            vowels += 1
        else:
            consonants += 1

        return f"vowels: {vowels}, consonants: {consonants}"

    print(count_characters("hello world"))