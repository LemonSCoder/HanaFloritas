#Might add part of speech system later (pronouns, verbs, and nouns. Only looking for adjectives and nouns.)
import re
import sys
import nltk
import part_of_speech
#Resolves problem where ntlk could not be imported.
nltk.download()
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.metrics import edit_distance
from collections import Counter
#Just a little side note: The name 'HanaFloritas' refers to the words 'Hana' (meaning flower in Japanese) and 'Floritas' (meaning little flowers in Spanish) within it
import random
import flowerModule
print("Welcome to HanaFloritas, a program that draws your flowers for you!")
flower_names = {
    "Rose" : ["love", "royalty", "beauty", "secrecy"], "Daffodil" : ["rebirth", "new", "hope", "joy", "luck"], "Carnation" : ["devotion", "love", "fascination"], "Lily" : ["love", "purity", "fertility", "rebirth"], "Daisy" : ["pur", "birth", "new", "cheer"], "Random" : [],
}
while True:
    #Experimenting around here
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    stop_words = stopwords.words('english')
    prompt = word_tokenize(re.sub('\W+', ' ', input("What is your prompt? > ")))
    lemmatized_text = [lemmatizer.lemmatize(token) for token in prompt]
    stopped_text = [word for word in prompt if word not in stop_words]
    lemmatized_stop_text = [lemmatizer.lemmatize(token) for token in stopped_text]
    #Code should eventually knock out any words that aren't nouns or adjectives so that they can appear. Might use the nltk tree too. Should only take one prompt (at least, if I'm lucky).
    #Might use Levenshtein distance to correct any spelling errors one makes.
    flower_names_list = ["Rose", "Daffodil", "Carnation", "Lily", "Tulip", "Daisy", "Flower"]
    flower_count_list = []
    override_list = []
    petal_number = []
    flower_number = []
    for word in lemmatized_stop_text:
        distance_to_petals = edit_distance("petal", word)
        distance_to_flowers = edit_distance("flowers", word)
        if distance_to_petals <= 3:
            word = "petal"
            continue
        for synonym in part_of_speech.get_synonyms(word):
            for i in range(10):
                if str(i) == synonym.lower() or str(i) in synonym.lower():
                    word = str(synonym)
                    #Add to check flower number or petal number: it's ngrams time!
                    bigrams = ngrams(lemmatized_stop_text, 2)
                    trigrams = ngrams(lemmatized_stop_text, 3)
                    for bigram in bigrams:
                        for flower_name in flower_names_list:
                            if str(word) and flower_name.lower() in bigram:
                                flower_number.append(word)
                        if str(word) and "petal" in bigram:
                            petal_number.append(word)
                    for trigram in trigrams:
                        if str(word) in trigram and flower_name.lower() in trigram:
                            flower_number.append(word)
                        elif str(word) in trigram and "petal" in trigram:
                            flower_number.append(word)
        for flower_name in flower_names_list:
            if word in flower_name.lower():
                override_list.append(word)
        for flower_name, description in flower_names.items():
            for trait in description:
                for synonym in part_of_speech.get_synonyms(word):
                    if trait in synonym or trait in word:
                        flower_count_list.append(flower_name)
                    else:
                        continue
    flower_counter = Counter()
    highest_flower_type = []
    if len(override_list) == 0:
        for flower_type in flower_count_list:
            if flower_counter[flower_type] > flower_counter[highest_flower_type]:
                for flower_name in flower_count_list:
                    if flower_name == highest_flower_type:
                        flower_count_list.remove(highest_flower_type)
                    else:
                        continue
                highest_flower_type = flower_type
            elif flower_counter[flower_type] < flower_counter[highest_flower_type] or flower_counter[flower_type] == flower_counter[highest_flower_type]:
                for flower_name in flower_count_list:
                    if flower_name == flower_type:
                        flower_count_list.remove(flower_type)
                    else:
                        continue
            else:
                highest_flower_type = flower_type
    elif len(override_list) > 0:
        while len(override_list) > 1:
            override_list.pop(-1)
        highest_flower_type = override_list[0]
    else:
        highest_flower_type = override_list[0]
    if len(flower_number) > 0:
        while len(flower_number) > 1:
            flower_number.pop(-1)
    if len(petal_number) > 0:
        while len(petal_number) > 1:
            petal_number.pop(0)
    if len(petal_number) > 0 and len(flower_number) > 0:
        if int(petal_number[0]) > 0 and int(petal_number[0]) <= 10 and int(flower_number[0]) > 0 and int(flower_number[0]) <= 10 and highest_flower_type != " ":
            flowerDrawn = flowerModule.flower(lemmatized_stop_text, str(petal_number), str(flower_number), str(highest_flower_type))
            flowerDrawn.get_flower()
        elif int(petal_number[0]) > 0 and int(petal_number[0]) <= 10 and int(flower_number[0]) > 0 and int(flower_number[0]) <= 10 and len(highest_flower_type) == 0:     
            flowerDrawn = flowerModule.flower(lemmatized_stop_text, str(petal_number), str(flower_number), random.choice(flower_names_list))  
            flowerDrawn.get_flower()
    elif len(petal_number) > 0:
        if int(petal_number[0]) > 0 and int(petal_number[0]) <= 10 and len(flower_number) == 0 and len(highest_flower_type) != 0:     
            flowerDrawn = flowerModule.flower(lemmatized_stop_text, str(petal_number), '[[1]', str(highest_flower_type))  
            flowerDrawn.get_flower()
        elif int(petal_number[0]) > 0 and int(petal_number[0]) <= 10 and len(flower_number) == 0 and len(highest_flower_type) == 0:     
            flowerDrawn = flowerModule.flower(lemmatized_stop_text, str(petal_number), '[[1]', random.choice(flower_names_list))  
            flowerDrawn.get_flower()
    elif len(flower_number) > 0:
        if len(petal_number) == 0 and int(flower_number[0]) > 0 and int(flower_number[0]) <= 10 and len(highest_flower_type) != 0:
            flowerDrawn = flowerModule.flower(lemmatized_stop_text, '[[5]', str(flower_number), str(highest_flower_type))
            flowerDrawn.get_flower()
        elif len(petal_number) == 0 and int(flower_number[0]) > 0 and int(flower_number[0]) <= 10 and len(highest_flower_type) == 0:     
            flowerDrawn = flowerModule.flower(lemmatized_stop_text, '[[5]', str(flower_number), random.choice(flower_names_list))  
            flowerDrawn.get_flower()
    else:
        if len(petal_number) == 0 and len(flower_number) == 0 and len(highest_flower_type) != 0:     
            flowerDrawn = flowerModule.flower(lemmatized_stop_text, '[[5]', '[[1]', str(highest_flower_type))  
            flowerDrawn.get_flower()
        else:
            flowerDrawn = flowerModule.flower(lemmatized_stop_text, '[[5]', '[[1]', "random") 
            flowerDrawn.get_flower()
    are_you_done = input("Do you want us to stop drawing flowers? \n [A] YES \n [B] NO \n > ")
    if "A" in are_you_done.upper():
        print("Goodbye.")
        sys.exit()
    else:
        continue
