import random

# Hangman Visual Stages
HANGMAN_STAGES = [
    """
       --------
       |      |
       |
       |
       |
       |
    -------- """,
    """
       --------
       |      |
       |      O
       |
       |
       |
    -------- """,
    """
       --------
       |      |
       |      O
       |      |
       |
       |
    -------- """,
    """
       --------
       |      |
       |      O
       |     /|
       |
       |
    -------- """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |
       |
    -------- """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     /
       |
    -------- """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / \\
       |
    -------- """
]

# Advanced Categorized Word Bank
WORD_BANK = {
    "easy": {
        "apple": "A famous crunchy fruit, often red or green",
        "school": "A place where students go to learn",
        "garden": "A beautiful place with plants and flowers",
        "tiger": "The national animal of India with stripes"
    },
    "medium": {
        "python": "A popular programming language named after a snake",
        "computer": "An electronic machine used for work and gaming",
        "guitar": "A musical instrument with six strings",
        "captain": "The leader of a ship or a sports team"
    },
    "hard": {
        "cryptography": "The art of writing or solving codes",
        "astronaut": "A person trained to travel in a spacecraft",
        "algorithm": "A step-by-step process used in coding to solve problems",
        "paradox": "A statement that contradicts itself but might be true"
    }
}

def choose_difficulty():
    """User se difficulty level choose karwane ke liye"""
    while True:
        print("\n--- CHOOSE YOUR DIFFICULTY ---")
        print("1. Easy   (Simple words, 8 Lives)")
        print("2. Medium (Normal words, 6 Lives)")
        print("3. Hard   (Tough words, 4 Lives)")
        choice = input("Enter choice (1/2/3 or Easy/Medium/Hard): ").lower().strip()
        
        if choice in ['1', 'easy']: return 'easy', 8
        if choice in ['2', 'medium']: return 'medium', 6
        if choice in ['3', 'hard']: return 'hard', 4
        print("⚠ Invalid Choice! Please choose a valid level.")

def play_game():
    total_score = 0
    print("==================================================")
    print("      🎮 ULTIMATE HANGMAN PRO: EDITION 2026 🎮")
    print("==================================================")
    
    while True:
        # 1. Level Selection
        level, max_lives = choose_difficulty()
        
        # Word selection based on level
        word_pool = WORD_BANK[level]
        word = random.choice(list(word_pool.keys()))
        hint = word_pool[word]
        
        guessed_letters = []
        wrong_guesses = 0
        perfect_game = True # Bonus score ke liye check
        
        print(f"\n🚀 Game Started! Level: {level.upper()} | Total Lives: {max_lives}")
        print(f"💡 Hint: {hint}")
        
        while wrong_guesses < max_lives:
            # Stage map karne ke liye formula taaki lives ke hisab se sahi drawing dikhe
            stage_index = int((wrong_guesses / max_lives) * 6)
            print(HANGMAN_STAGES[stage_index])
            
            # Display current word status
            display_word = " ".join([char if char in guessed_letters else "_" for char in word])
            print(f"\nWord: {display_word}")
            print(f"Guessed Letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
            print(f"Remaining Lives: {max_lives - wrong_guesses} ❤️")
            
            # Win Check
            if "_" not in display_word:
                print(f"\n🎉 BOOM! You guessed it! The word was: {word.upper()}")
                
                # Points calculation
                base_points = 10 if level == 'easy' else (20 if level == 'medium' else 30)
                if perfect_game:
                    print("🔥 PERFECT MATCH BONUS! (+10 extra points)")
                    base_points += 10
                    
                total_score += base_points
                print(f"⭐ Score Added! Current Total Score: {total_score}")
                break
                
            guess = input("\nEnter a letter: ").lower().strip()
            
            # Validations
            if len(guess) != 1 or not guess.isalpha():
                print("⚠ Oops! Please enter exactly ONE alphabet letter.")
                continue
                
            if guess in guessed_letters:
                print(f"⚠ You already tried '{guess}'. Koi naya letter socho!")
                continue
                
            guessed_letters.append(guess)
            
            # Process Guess
            if guess in word:
                print("✅ Bullseye! Correct guess.")
            else:
                print("❌ Ouch! Wrong guess.")
                wrong_guesses += 1
                perfect_game = False

        # Lose Check
        if wrong_guesses == max_lives:
            print(HANGMAN_STAGES[6]) # Full hangman drawing
            print(f"\n💀 GAME OVER! The executioner won.")
            print(f"The correct word was: {word.upper()}")
            print(f"Your Total Score: {total_score}")
            
        # Replay Option
        play_again = input("\nDo you want to challenge yourself again? (yes/no): ").lower().strip()
        if play_again != 'yes':
            print("\n==================================================")
            print(f"🏆 FINAL LEADERBOARD SCORE: {total_score} POINTS")
            print("Thanks for playing Ultimate Hangman. See ya! 👋")
            print("==================================================")
            break

if __name__ == "__main__":
    play_game()