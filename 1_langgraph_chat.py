import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, MessagesState, StateGraph


def build_chat_workflow():
	"""Build a LangGraph workflow for a conversational assistant."""
	model = ChatOpenAI(
		model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
		temperature=0.7,
	)

	def call_model(state: MessagesState) -> dict[str, list[BaseMessage]]:
		response = model.invoke(
			[
				# {
				# 	"role": "system",
				# 	"content": "You are a helpful assistant. Keep answers clear and concise.",
				# },
				SystemMessage(content="You are a helpful assistant. Respond in one or 2 words only."),
				*state["messages"],
			]
		)
		return {"messages": [response]}

	workflow = StateGraph(MessagesState)
	workflow.add_node("assistant", call_model)
	workflow.add_edge(START, "assistant")
	workflow.add_edge("assistant", END)
	return workflow.compile()


def run_chat() -> None:
	"""Run an interactive terminal chat with graph-managed messages."""
	if not os.getenv("OPENAI_API_KEY"):
		raise RuntimeError("Set OPENAI_API_KEY before starting the chat.")

	chat_workflow = build_chat_workflow()
	history: list[BaseMessage] = []

	print("LangGraph chat started. Type 'exit' or 'quit' to leave.")
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

		result = chat_workflow.invoke(
			{"messages": [*history, HumanMessage(content=user_input)]}
		)

		history = result["messages"]
		print ("History:", history)
		print(f"Assistant: {history[-1].content}")


if __name__ == "__main__":
	run_chat()
