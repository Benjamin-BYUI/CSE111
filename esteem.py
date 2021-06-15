def get_score(posneg, letter):
    if posneg == "pos":
        if letter == "D":
            return 0
        elif letter == "d":
            return 1
        elif letter == "a":
            return 2
        else:
            return 3
    else:
        if letter == "D":
            return 3
        elif letter == "d":
            return 2
        elif letter == "a":
            return 1
        else:
            return 0

print("This program is an implementation of the Rosenberg Self-Esteem Scale.\n"
"This program will show you ten statements that you could possibly\n"
"apply to yourself. Please rate how much you agree with each of the\n"
"statements by responding with one of these four letters:")
print()
print("D means you strongly disagree with the statement.\n"
"d means you disagree with the statement.\n"
"a means you agree with the statement.\n"
"A means you strongly agree with the statement.")
print()
score = 0
print("1. I feel that I am a person of worth, at least on an equal plane with others.")
letter = input("Enter D, d, a, or A: ")
score += get_score("pos", letter)
print("2. I feel that I have a number of good qualities.")
letter = input("Enter D, d, a, or A: ")
score += get_score("pos", letter)
print("3. All in all, I am inclined to feel that I am a failure.")
letter = input("Enter D, d, a, or A: ")
score += get_score("neg", letter)
print("4. I am able to do things as well as most other people.")
letter = input("Enter D, d, a, or A: ")
score += get_score("pos", letter)
print("5. I feel I do not have much to be proud of.")
letter = input("Enter D, d, a, or A: ")
score += get_score("neg", letter)
print("6. I take a positive attitude toward myself.")
letter = input("Enter D, d, a, or A: ")
score += get_score("pos", letter)
print("7. On the whole, I am satisfied with myself.")
letter = input("Enter D, d, a, or A: ")
score += get_score("pos", letter)
print("8. I wish I could have more respect for myself.")
letter = input("Enter D, d, a, or A: ")
score += get_score("neg", letter)
print("9. I certainly feel useless at times.")
letter = input("Enter D, d, a, or A: ")
score += get_score("neg", letter)
print("10. At times I think I am no good at all.")
letter = input("Enter D, d, a, or A: ")
score += get_score("neg", letter)
print()
print(f"Your score is {score}.")
print("A score below 15 may indicate problematic low self-esteem.")