import random

# DATA is internal to the script for reliability.
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
    },
    {
        "reference": "Revelation 21:4",
        "text": "And he will wipe out every tear from their eyes, and death will be no more...",
        "missing_word": "death",
        "trivia_question": "According to Revelation 21:4, what will be no more?",
        "options": ["Death", "Sickness", "Pain", "Crying"]
    },
    {
        "reference": "2 Timothy 3:16",
        "text": "All Scripture is inspired of God and beneficial for teaching...",
        "missing_word": "inspired",
        "trivia_question": "How does 2 Timothy 3:16 describe all Scripture?",
        "options": ["Inspired of God", "A good history", "Written by men", "Ancient wisdom"]
    },
    {
        "reference": "Proverbs 3:5",
        "text": "Trust in Jehovah with all your heart, and do not rely on your own understanding.",
        "missing_word": "understanding",
        "trivia_question": "What should we not rely on, according to Proverbs 3:5?",
        "options": ["Your own understanding", "Your friends", "Wealth", "The law"]
    }
]

def play_trivia(item):
    print(f"\n--- TRIVIA: {item['reference']} ---")
    print(item['trivia_question'])
    for i, option in enumerate(item['options'], 1):
        print(f"{i}. {option}")

    try:
        choice = int(input("\nYour answer (1-4): "))
        if item['options'][choice - 1] == item['options'][0]:
            print("Correct! 🌟")
        else:
            print(f"Not quite. The correct answer was: {item['options'][0]}")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number between 1 and 4.")

def play_fill_in(item):
    print(f"\n--- FILL IN THE BLANK: {item['reference']} ---")
    display_text = item['text'].replace(item['missing_word'], "_______")
    print(display_text)
    answer = input("\nWhat is the missing word? ").strip()

    if answer.lower() == item['missing_word'].lower():
        print("Exactly right! ✨")
    else:
        print(f"Close! The word was '{item['missing_word']}'.")

def main():
    print("========================================")
    print("   WELCOME TO THE SCRIPTURE CHALLENGE   ")
    print("========================================")

    while True:
        scripture = random.choice(DATA)
        print("\n1. Trivia Mode (Multiple Choice)")
        print("2. Fill-in-the-Blank")
        print("3. Exit Game")

        mode = input("\nChoose a mode (1, 2, or 3): ")

        if mode == "1":
            play_trivia(scripture)
        elif mode == "2":
            play_fill_in(scripture)
        elif mode == "3":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()