print("Welcome to Mad Lib!")
print("Here are the list of words our game allows: \n 1. Nouns \n 2. Adjectives \n 3. Verbs")
word_type = int(input("Specify the type of word by entering it's number: "))

if word_type < 1 or word_type > 3:
    print("You've chosen invalid choice! Try again.")
    
elif word_type == 1:
    chosen_word =input("Enter the word: ")
    print("One day, a mysterious", chosen_word, "appeared in my backyard. At first, I thought it was a dream. But then the",chosen_word, "started to dance and sing! \n By the end of the day, the entire neighborhood had gathered around to watch the famous ", chosen_word, " perform.")
    
elif word_type == 2:
    chosen_word =input("Enter the word: ")
    print("It was a", chosen_word,"morning. The sky was ", chosen_word, ", my cereal tasted ", chosen_word,", and even my dog looked unusually",chosen_word, ". I had a feeling this would be no ordinary day — and I was absolutely right.")
    
elif word_type == 3:
    chosen_word =input("Enter the word: ")
    print("Every Saturday, I",chosen_word,"down the street to the bakery. One time, I ",chosen_word, "o quickly that I passed five people and scared a pigeon. Now, whenever I",chosen_word, ", people step aside, knowing I’m on a serious pastry mission.")
