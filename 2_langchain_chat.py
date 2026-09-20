import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI


def build_chat_chain() -> object:
	"""Build a LangChain prompt-to-model chat workflow."""
	prompt = ChatPromptTemplate.from_messages(
		[
			(
				"system",
				"You are a helpful assistant. Keep answers clear and concise.",
			),
			MessagesPlaceholder(variable_name="history"),
			("human", "{input}"),
		]
	)
	model = ChatOpenAI(
		model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
		temperature=0.7,
	)
	return prompt | model


def run_chat() -> None:
	"""Run an interactive terminal chat with conversational memory."""
	if not os.getenv("OPENAI_API_KEY"):
		raise RuntimeError("Set OPENAI_API_KEY before starting the chat.")

	chat_chain = build_chat_chain()
	history: list[BaseMessage] = []

	print("LangChain chat started. Type 'exit' or 'quit' to leave.")
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

		response = chat_chain.invoke({"history": history, "input": user_input})
		answer = response.content
		print(f"Assistant: {answer}")
		history.extend(
			[HumanMessage(content=user_input), AIMessage(content=answer)]
		)


if __name__ == "__main__":
	run_chat()


