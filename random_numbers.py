import random

def main():
    randnums = [16.2, 75.1, 52.3]
    print(randnums)
    append_random_numbers(randnums)
    print(randnums)
    append_random_numbers(randnums, 3)
    print(randnums)

    randwords = ["shark"]
    print(randwords)
    append_random_words(randwords)
    print(randwords)
    append_random_words(randwords, 3)
    print(randwords)

def append_random_numbers(number_list, quantity = 1):
    for _ in range(quantity):
        number_list.append(round(random.uniform(0, 100), 1))

def append_random_words(words_list, quantity = 1):
    words = ["dog", "cat", "bird", "aligator", "raptor", "fish", "Add" ,"something", "or", "change"]
    for _ in range(quantity):
        words_list.append(random.choice(words))

if __name__ == "__main__":
    main()