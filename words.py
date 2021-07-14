import random 

def load_words():
    f=open("words.txt","r")
    data=f.read().split()
    return data
def choose_words():
    word_list=load_words()
    secret_word=random.choice(word_list)
    secret_word=secret_word.lower()
    return secret_word
    
    
    

