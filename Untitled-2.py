print('Hello everyone')
print('WELCOME')
print('GAMING PROJECT')

# Check if the user wants to play
playing = input('Would you like to play? ').lower()
if playing != "yes":
    print("Goodbye!")
    quit()

print('Welcome to the game :)')
score = 0
total_questions = 6

# --- THE EPL CATALOG ---
epl_catalog = ["arsenal", "chelsea", "man city", "liverpool", "man united"]

# --- QUESTION 1 WITH VALIDATION ---
# This loop prevents mismatches by checking the input against your catalog
print(f"\nChoose a team from our catalog: {', '.join([t.title() for t in epl_catalog])}")

while True:
    answer = input('Your choice: ').lower()
    if answer in epl_catalog:
        print(f'Correct! {answer.title()} is in the EPL catalog. ✅')
        score += 1
        break # This exits the loop once a valid choice is made
    else:
        print(f"❌ '{answer}' is not in the list. Please choose from: {', '.join(epl_catalog)}")

# --- REMAINING QUESTIONS ---
# Question 2
answer = input('\n2. Will Arsenal win the Premier League? ').lower()
if answer == 'no':
    print('Correct! ❌🏆')
    score += 1 # Fixed scoring logic
else:
    print('Try again!')

# Question 3
answer = input('3. What is G.O.A.T? ').lower()
if answer == 'greatest of all time':
    print('Correct! 🐐')
    score += 1 # Corrected from score=+1
else:
    print('Try again!')

# Question 4
answer = input('4. Who is better Messi or Ronaldo? ').lower()
if answer == 'ronaldo':
    print('Correct! SIUUU! 🇵🇹')
    score += 1
else:
    print('Try again!')

# Question 5
answer = input('5. Which team was knocked out of Europa? ').lower()
if answer == 'arsenal': # Simplified from lower().upper()
    print('Correct! ⚽')
    score += 1
else:
    print('Try again!')

# Question 6
answer = input('6. Which team is known as Nduthi Fc? ').lower()
if answer == 'chelsea':
    print('Correct! 🏍️')
    score += 1
else:
    print('Try again!')

# --- FINAL SCOREBOARD ---
print("\n" + "="*30)
print(f"GAME OVER, {score}/{total_questions} CORRECT!")
print(f"Percentage Score: {int((score / total_questions) * 100)}%")
print("="*30)

