from typesafe_sdk import Choice, Noul, Score, TypeSafeClient
from dotenv import load_dotenv
load_dotenv()

client = TypeSafeClient()


def get_jev_response(user_input: str):
    response = client.system_one(
        state={"item": user_input},
        questions={
            "is_food": Noul(
                instructions="Is this `item` a food?"
            ),
            "cuisine": Choice(
                instructions="What type of cuisine is `item`?",
                criteria={
                    "Indian": None,
                    "Chinese": None,
                    "Italian": None,
                    "Mediterranean": None,
                    "European": None,
                    "American": None,
                    "Thai": None,
                    "African": None,
                    "Mexican": None,
                    "Latin": None,
                    "Other": None,
                },
            ),
            "sweetness": Score(
                instructions="How sweet is `item`?",
                criteria=[
                    "Not sweet",
                    "mild sweet",
                    "medium sweet",
                    "very sweet",
                    "extreme sweet",
                ],
            ),
        },
    )
    return response


def run_chat() -> None:
    """Run an interactive terminal chat with conversational memory."""
    print("Jev session started. Type name of food or 'exit' or 'quit' to leave.")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return

        if not user_input:
            continue

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            return

        jev_response = get_jev_response(user_input)
        print(f"is_food: {jev_response.answers["is_food"].noul}")
        print(f"cuisine: {jev_response.answers["cuisine"].choice}")
        print(f"cuisine probability: {jev_response.answers["cuisine"].probabilities}")
        print(f"sweetness level : {jev_response.answers["sweetness"].score}\n")


if __name__ == "__main__":
    run_chat()
