#gets a sentence from a user and converts it to Pig Latin then returns it to user

# get sentence from user
original = input('Please enter a sentence: ').strip().lower()

#split sentence into words
words = original.split()

# loop through words and convert to pig latin
new_words = []

for word in words:
    if word[0] in "aeiou": #for words starting with a vowel, add 'yay'
        add_word = word + 'yay'
    else: # for words starting with consonants, take first consonant cluster and move to back, then add 'ay'
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos += 1
            else:
                break
        add_word = word[vowel_pos:] + word[:vowel_pos] + 'ay'
    new_words.append(add_word)

# stick words back together into sentence
output = " ".join(new_words)

# output the final string
print(output)