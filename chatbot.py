import string

RESPONSES = {
    "hello": "Hi!",
    "hi": "Hi!",
    "hey": "Hi!",
    "how are you": "I'm fine, thanks!",
    "what is your name": "I'm a simple Python chatbot.",
    "help": "You can say hello, ask how I am, or say bye to exit.",
    "bye": "Goodbye!",
    "exit": "Goodbye!",
    "quit": "Goodbye!",
}
EXIT_MESSAGES = {"bye", "exit", "quit"}
UNKNOWN_RESPONSE = "Sorry, I don't understand that. Type 'help' to see what I can answer."
EMPTY_RESPONSE = "Please enter a message."


def normalize_message(message: str) -> str:
    if not isinstance(message, str):
        return ""

    collapsed_spaces = " ".join(message.lower().split())
    return collapsed_spaces.strip(string.punctuation)


def get_response(message: str) -> str:
    normalized_message = normalize_message(message)
    if not normalized_message:
        return EMPTY_RESPONSE

    return RESPONSES.get(normalized_message, UNKNOWN_RESPONSE)


def should_exit(message: str) -> bool:
    return normalize_message(message) in EXIT_MESSAGES


def chatbot() -> None:
    print("========== PYTHON CHATBOT ==========")
    print("Bot: Hello! I'm a simple rule-based chatbot. Type 'help' for examples.")

    while True:
        user_message = input("You: ")
        response = get_response(user_message)
        print(f"Bot: {response}")

        if should_exit(user_message):
            break


def main() -> None:
    chatbot()


if __name__ == "__main__":
    main()
