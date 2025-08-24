import random

ENCOURAGING_QUOTES = [
    "Great job!",
    "Keep it up!",
    "You're doing awesome!",
    "Fantastic effort!",
    "Nice work!",
    "Keep pushing!",
    "You're a math star!",
    "Impressive!",
    "Way to go!",
    "You can do it!"
]

def get_player_name():
    name = input("What's your name? ")
    return name.strip() or "Player"

def get_difficulty():
    while True:
        try:
            level = int(input("Choose your difficulty level (1-10): "))
            if 1 <= level <= 10:
                return level
            else:
                print("Please enter a number from 1 to 10.")
        except ValueError:
            print("Please enter a valid number.")

def display_question(difficulty):
    a = random.randint(1, difficulty * 2)
    b = random.randint(1, difficulty * 2)
    print(f"What is {a} x {b}?")
    return a, b

def get_answer():
    try:
        return int(input("Your answer: "))
    except ValueError:
        print("Please enter a valid number.")
        return get_answer()

def check_answer(a, b, user_answer):
    return user_answer == a * b

def update_score(score, correct):
    if correct:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer was {a * b}.")
    print(random.choice(ENCOURAGING_QUOTES))
    return score

def quiz_game(num_questions=5):
    print("Welcome to the Multiplication Quiz Game!")
    player_name = get_player_name()
    print(f"Hello, {player_name}! Let's test your multiplication skills.")
    difficulty = get_difficulty()
    print(f"You selected difficulty level {difficulty}. Good luck!\n")
    score = 0

    for i in range(num_questions):
        print(f"\nQuestion {i+1}:")
        a, b = display_question(difficulty)
        user_answer = get_answer()
        correct = check_answer(a, b, user_answer)
        score = update_score(score, correct)

    print(f"\nGame Over, {player_name}! Your final score is {score} out of {num_questions}.")
    if score == num_questions:
        print("Amazing! You got all the questions right!")
    elif score > num_questions // 2:
        print("Well done! Keep practicing to get even better!")
    else:
        print("Don't give up! Practice makes perfect!")

if __name__ == "__main__":
    quiz_game()