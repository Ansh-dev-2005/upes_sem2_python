def random_code():
    import random
    code = ""
    for i in range(4):
        code += str(random.randint(0,9))
    return code

def check_code(code, guess):
    result = ""
    for i in range(4):
        if guess[i] == code[i]:
            result += "R"
        elif guess[i] in code:
            result += "Y"
        else:
            result += "B"
    return result

def main():
    code = random_code()
    for i in range(10):
        print("You have", 10-i, "tries left.")
        guess = input("Enter a 4-digit code: ")
        
        # check if guess is a 4-digit number
        if not guess.isdigit() or len(guess) != 4:
            print("Invalid guess. Please enter a 4-digit number.")
            continue
        
        if guess == code:
            print("You won!")
            break
        else:
            print(check_code(code, guess))
    
    # if the loop completes without breaking, the user has lost
    else:
        print("You lost! The code was", code)

# run the game
main()
