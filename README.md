# AI Playground

This project serves as an experimental playground for testing various AI and Python features. It provides a sandbox environment to explore and prototype different AI frameworks, chat implementations, and Python development workflows.

## Project Overview

The AI Playground is designed to:
- Test different AI frameworks (LangChain, LangGraph)
- Experiment with Python development workflows
- Prototype chat and conversational AI applications
- Validate development tooling and dependency management

## Project Structure

```
.
├── 1_langgraph_chat.py      # LangGraph-based chat implementation
├── 2_langchain_chat.py       # LangChain-based chat implementation  
├── main.py                   # Basic entry point
├── pyproject.toml            # Project dependencies and configuration
├── README.md                 # This file
├── .env                      # Environment variables
├── .venv/                    # Virtual environment
└── uv.lock                   # Dependency lock file
```

## Key Features Being Tested

### 1. AI Frameworks
- **LangGraph**: State management and workflow orchestration
- **LangChain**: Chain-based language model applications
- **OpenAI Integration**: API connectivity and model interactions

### 2. Development Tools
- **uv**: Modern Python package manager and dependency resolver
- **Virtual Environments**: Isolated Python development
- **dotenv**: Environment variable management

### 3. Application Types
- **Chat Applications**: Interactive conversational interfaces
- **Workflow Management**: State machine and graph-based workflows
- **Message Handling**: Structured message processing

## Getting Started

### Prerequisites

- Python 3.13 or higher
- uv package manager (recommended)

### Installation

```bash
# Clone the repository
cd /path/to/ai-playground

# Create and activate virtual environment
uv venv
.venv/bin/activate

# Install dependencies
uv sync
```

### Running Examples

#### Basic Test
```bash
# Run the main entry point
uv run main.py
```

#### LangGraph Chat
```bash
# Run the LangGraph chat implementation
uv run 1_langgraph_chat.py
```

#### LangChain Chat
```bash
# Run the LangChain chat implementation
uv run 2_langchain_chat.py
```

### Environment Setup

Create a `.env` file with your API keys:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

## Technologies Used

- **Python**: 3.13+
- **uv**: Package manager and dependency resolver
- **LangChain**: Language model application framework
- **LangGraph**: State management and workflow framework
- **OpenAI**: Language model API
- **dotenv**: Environment variable management

## Development Workflow

This project follows a test-driven approach to:
1. Validate new AI frameworks and libraries
2. Test Python development workflows
3. Prototype chat and conversational AI features
4. Experiment with modern tooling

## Contributing

This is an experimental project, so contributions are welcome for:
- New AI framework integrations
- Additional chat implementations
- Development tooling improvements
- Documentation updates

## License

This project is for experimental purposes and is not intended for production use.

## Support

For issues or questions, please refer to the project structure and examples above.