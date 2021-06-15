from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest


def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one", "a"]
    # This loop will repeat the statements inside it 6 times.
    for _ in range(6):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many", "two"]
    for _ in range(6):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # Test the singular nouns.
    singular_nouns = ["bird", "boy", "car", "cat",
                      "child", "dog", "girl", "man", "woman"]
    # This loop will repeat the statements inside it 18 times.
    for _ in range(18):
        noun = get_noun(1)

        # Verify that the noun returned from get_noun is
        # one of the nouns in the singular_nouns list.
        assert noun in singular_nouns

    # Test the plural nouns.
    plural_nouns = ["adults", "birds", "boys", "cars", "cats",
                    "children", "dogs", "girls", "men", "women"]
    for _ in range(20):
        noun = get_noun(2)

        # Verify that the noun returned from get_noun
        # is one of the nouns in the plural_nouns list.
        assert noun in plural_nouns

def test_get_verb():
    # Test the past tense verbs.
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
                  "ran", "slept", "talked", "walked", "wrote"]
    # This loop will repeat the statements inside it 20 times.
    for _ in range(20):
        verb = get_verb(1, "past")

        # Verify that the verb returned from get_verb is
        # one of the verbs in the past_verbs list.
        assert verb in past_verbs

    # Test the singular present tense verbs.
    singular_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                              "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(20):
        verb = get_verb(1, "present")

        # Verify that the verb returned from get_verb is
        # one of the verbs in the singular_present_verbs list.
        assert verb in singular_present_verbs
    
    # Test the plural present tense verbs.
    plural_present_verbs = ["drink", "eat", "grow", "laugh", "think",
                            "run", "sleep", "talk", "walk", "write"]
    for _ in range(20):
        verb = get_verb(2, "present")

        # Verify that the verb returned from get_verb is
        # one of the verbs in the plural_present_verbs list.
        assert verb in plural_present_verbs
    
    # Test the future tense verbs.
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
                    "will think", "will run", "will sleep", "will talk",
                    "will walk", "will write"]
    for _ in range(20):
        verb = get_verb(1, "future")

        # Verify that the verb returned from get_verb is
        # one of the verbs in the future_verbs list.
        assert verb in future_verbs

def test_get_preposition():
    prepositions = ["for", "above", "off", "at", "on", "about"]
    # This loop will repeat the statements inside it 12 times.
    for _ in range(12):
        preposition = get_preposition()

        # Verify that the preposition returned from get_preposition is
        # one of the prepositions in the prepositions list.
        assert preposition in prepositions

def test_get_prepositional_phrase():
    # Test the singular prepositional phrases.
    prepositions = ["for", "above", "off", "at", "on", "about"]
    singular_nouns = ["bird", "boy", "car", "cat",
                      "child", "dog", "girl", "man", "woman"]
    singular_determiners = ["the", "one", "a"]
    # This loop will repeat the statements inside it 36 times.
    for _ in range(36):
        prepositional_phrase = get_prepositional_phrase(1)
        preposition, singlular_determiner, singular_noun = prepositional_phrase.split(" ")

        # Verify that the preposition returned from get_prepositional_phrase is
        # one of the prepositions in the prepositions list.
        assert preposition in prepositions

        # Verify that the noun returned from get_prepositional_phrase is
        # one of the nouns in the singular_nouns list.
        assert singular_noun in singular_nouns

        # Verify that the determiner returned from get_prepositional_phrase is
        # one of the determiners in the singular_determiners list.
        assert singlular_determiner in singular_determiners
    
    # Test the plural prepositional phrases.
    plural_nouns = ["adults", "birds", "boys", "cars", "cats",
                    "children", "dogs", "girls", "men", "women"]
    plural_determiners = ["some", "many", "two"]
    # This loop will repeat the statements inside it 34 times.
    for _ in range(34):
        prepositional_phrase = get_prepositional_phrase(2)
        preposition, plural_determiner, plural_noun = prepositional_phrase.split(" ")

        # Verify that the preposition returned from get_prepositional_phrase is
        # one of the prepositions in the prepositions list.
        assert preposition in prepositions

        # Verify that the noun returned from get_prepositional_phrase is
        # one of the nouns in the plural_nouns list.
        assert plural_noun in plural_nouns

        # Verify that the determiner returned from get_prepositional_phrase is
        # one of the determiners in the plural_determiners list.
        assert plural_determiner in plural_determiners

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])