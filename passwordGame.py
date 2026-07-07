import itertools,string,time

PASSWORD = "ghtf"
ALLOWED_CHARS = string.ascii_lowercase


def brute_force_password(target: str, allowed: str = ALLOWED_CHARS):
    start_time = time.perf_counter()
    attempts = 0

    for candidate in itertools.product(allowed, repeat=len(target)):
        attempts += 1
        guess = "".join(candidate)
        if guess == target:
            elapsed = time.perf_counter() - start_time
            return guess, attempts, elapsed

    elapsed = time.perf_counter() - start_time
    return None, attempts, elapsed


def password_game():
    print("Welcome to the password guessing game.")
    print("Try to guess the 4-character secret password.")

    while True:
        attempts = 0
        start_time = time.perf_counter()

        while True:
            user_choice = input("Guess the password: ").lower()
            attempts += 1

            if user_choice == PASSWORD:
                elapsed = time.perf_counter() - start_time
                print("You guessed the password right!")
                print(f"Your attempts: {attempts}")
                print(f"Time taken: {elapsed:.2f} seconds")
                break

            print("You guessed the password wrong!")


        continue_game = input("Do you want to play again? (y/n): ").lower()
        if continue_game != "y":
            print("Thank you for playing!")
            break


if __name__ == '__main__':
    password_game()
          