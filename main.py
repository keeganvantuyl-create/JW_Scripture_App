import random

# DATA is now internal to the script to ensure 100% reliability
# while you move quickly on your Acer.
DATA = [
    {
        "reference": "Matthew 24:14",
        "text": "And this good news of the Kingdom will be preached in all the inhabited earth...",
        "missing_word": "Kingdom",
        "trivia_question": "What will be preached in all the inhabited earth according to Matthew 24:14?",
        "options": ["The Kingdom", "The Law", "The Prophecy", "The End"]
    },
    {
        "reference": "Psalm 83:18",
        "text": "May people know that you, whose name is Jehovah, You alone are the Most High over all the earth.",
        "missing_word": "Jehovah",
        "trivia_question": "According to Psalm 83:18, what is God's name?",
        "options": ["Jehovah", "The Lord", "The Creator", "The Almighty"]
    }
]


def play_trivia(item):
    print(f"\n--- TRIVIA: {item['reference']} ---")
    print(item['trivia_question'])

    # We display the options to the user
    for i, option in enumerate(item['options'], 1):
        print(f"{i}. {option}")

    try:
        choice = int(input("\nYour answer (1-4): "))
        # The first option in our list is always the correct one
        if item['options'][choice - 1] == item['options'][0]:
            print("Correct! 🌟")
        else:
            print(f"Not quite. The correct answer was: {item['options'][0]}")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number between 1 and 4.")


def play_fill_in(item):
    print(f"\n--- FILL IN THE BLANK: {item['reference']} ---")
    # Replace the target word with underscores for the challenge
    display_text = item['text'].replace(item['missing_word'], "_______")
    print(display_text)

    answer = input("\nWhat is the missing word? ").strip()

    if answer.lower() == item['missing_word'].lower():
        print("Exactly right! ✨")
    else:
        print(f"Close! The word was '{item['missing_word']}'.")


def main():
    # Randomly picks one scripture from our DATA list above
    scripture = random.choice(DATA)

    print("========================================")
    print("   WELCOME TO THE SCRIPTURE CHALLENGE   ")
    print("========================================")
    print("1. Trivia Mode (Multiple Choice)")
    print("2. Fill-in-the-Blank")

    mode = input("\nChoose a mode (1 or 2): ")

    if mode == "1":
        play_trivia(scripture)
    elif mode == "2":
        play_fill_in(scripture)
    else:
        print("Invalid choice. Restart the app to try again.")


if __name__ == "__main__":
    main()