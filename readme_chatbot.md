# CodeAlpha Project: Basic Chatbot

A beginner-friendly, rule-based console chatbot built with Python's standard library.

## Features

- Responds to `hello`, `hi`, and `hey` with a greeting.
- Responds to `how are you` with the required predefined reply.
- Supports `bye` as the required exit command; `exit` and `quit` also work.
- Handles uppercase/lowercase input, extra spaces, and common punctuation.
- Provides a friendly response for empty or unrecognized messages.
- Includes `help`, `what is your name`, and other small optional responses.

## Requirements

- Python 3.9 or newer (no third-party packages required).

## Run the chatbot

From this folder, run:

```bash
python chatbot.py
```

On some systems, use `python3 chatbot.py` instead.

## Run the tests

```bash
python -m unittest discover -s tests -v
```

The tests cover required replies, normalized input, unknown/empty messages, exit behavior, and multi-turn conversation.
