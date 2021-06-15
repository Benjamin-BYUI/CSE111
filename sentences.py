import random

def main():
    print(f"{get_determiner(1).capitalize()} {get_noun(1)} {get_verb(1, 'past')}.")
    print(f"{get_determiner(2).capitalize()} {get_noun(2)} {get_verb(2, 'past')}.")
    print(f"{get_determiner(1).capitalize()} {get_noun(1)} {get_verb(1, 'present')}.")
    print(f"{get_determiner(2).capitalize()} {get_noun(2)} {get_verb(2, 'present')}.")
    print(f"{get_determiner(1).capitalize()} {get_noun(1)} {get_verb(1, 'future')}.")
    print(f"{get_determiner(2).capitalize()} {get_noun(2)} {get_verb(2, 'future')}.")

    print(f"{get_determiner(1).capitalize()} {get_noun(1)} {get_verb(1, 'past')} {get_prepositional_phrase(1)}.")
    print(f"{get_determiner(2).capitalize()} {get_noun(2)} {get_verb(2, 'past')} {get_prepositional_phrase(2)}.")
    print(f"{get_determiner(1).capitalize()} {get_noun(1)} {get_verb(1, 'present')} {get_prepositional_phrase(1)}.")
    print(f"{get_determiner(2).capitalize()} {get_noun(2)} {get_verb(2, 'present')} {get_prepositional_phrase(2)}.")
    print(f"{get_determiner(1).capitalize()} {get_noun(1)} {get_verb(1, 'future')} {get_prepositional_phrase(1)}.")
    print(f"{get_determiner(2).capitalize()} {get_noun(2)} {get_verb(2, 'future')} {get_prepositional_phrase(2)}.")

    print(f"{get_determiner(1).capitalize()} {get_noun(1)} {get_verb(1, 'past')} {get_prepositional_phrase(1)} {get_prepositional_phrase(2)}.")
    print(f"{get_determiner(2).capitalize()} {get_noun(2)} {get_verb(2, 'past')} {get_prepositional_phrase(2)} {get_prepositional_phrase(1)}.")
    print(f"{get_determiner(1).capitalize()} {get_noun(1)} {get_verb(1, 'present')} {get_prepositional_phrase(1)} {get_prepositional_phrase(2)}.")
    print(f"{get_determiner(2).capitalize()} {get_noun(2)} {get_verb(2, 'present')} {get_prepositional_phrase(2)} {get_prepositional_phrase(1)}.")
    print(f"{get_determiner(1).capitalize()} {get_noun(1)} {get_verb(1, 'future')} {get_prepositional_phrase(1)} {get_prepositional_phrase(2)}.")
    print(f"{get_determiner(2).capitalize()} {get_noun(2)} {get_verb(2, 'future')} {get_prepositional_phrase(2)} {get_prepositional_phrase(1)}.")

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is a word
    like "the", "a", "one", "two", "some", "many". If quantity == 1,
    this function will return either "the" or "one". Otherwise
    this function will return either "some" or "many".

    Parameter
        quantity: an integer. If quantity == 1, this function will
            return a determiner for a singular noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["the", "one", "a"]
    else:
        words = ["some", "many", "two"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun. If quantity == 1, this
    function will return one of these ten singular nouns:
        "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these ten
    plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        quantity: an integer that determines if the
            returned noun is singular or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat",
                 "child", "dog", "girl", "man", "woman"]
    else:
        nouns = ["adults", "birds", "boys", "cars", "cats",
                 "children", "dogs", "girls", "men", "women"]

    # Randomly choose and return a noun.
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this function will
    return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1, this function
    will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of these
    ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        quantity: an integer that determines if the returned
            verb is singular or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present":
        verbs = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]
    else: # tense must be future.
        verbs = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]

    # Randomly choose and return a verb.
    verb = random.choice(verbs)
    return verb

def get_preposition():
    """Return a randomly chosen preposition. A preposition is a word
    like "for", "above", "off", "at", "on", "about". 

    Return: a randomly chosen preposition.
    """
    prepositions = ["for", "above", "off", "at", "on", "about"]

    # Randomly choose and return a preposition.
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
    return f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}"

# Begin program by calling main iff this file is being executed directly.
if __name__ == "__main__":
    main()