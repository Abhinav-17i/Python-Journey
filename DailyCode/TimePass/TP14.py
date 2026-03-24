import random

words = ["python", "lennox", "puzzle", "gaming", "computer"]

word = random.choice(words)

scrambled = ''.join(random.sample(word, len(word)))

print("Unscramble the word!")
print("Scrambled word:", scrambled)

attempts = 3

while attempts > 0:
    guess = input("Your guess: ").lower()

    if guess == word:
        print("🎉 Correct! You solved it!")
        break
    else:
        attempts -= 1
        print(f"❌ Wrong! Attempts left: {attempts}")

if attempts == 0:
    print(f"💀 Game Over! The word was '{word}'")