from nltk.corpus import wordnet
from collections import Counter
from itertools import chain
def get_part_of_speech(word):
    guessed_part_of_speech = wordnet.synsets(word)
    pos_count = Counter()
    for item in guessed_part_of_speech:
      if item.pos() == "n" or item.pos() == "a":
        pos_count["n/a"] += 1
      else:
        pos_count["other"] += 1
    #Rose is a flower but also the past tense of 'rise', so it is likely to be labeled a verb as a part of speech.
    if pos_count["n/a"] >= pos_count["other"] or word == "rose":
      return "Yes"
    else:
      return "No"

def get_synonyms(word):
  synonyms = wordnet.synsets(word)
  lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
  return lemmas
