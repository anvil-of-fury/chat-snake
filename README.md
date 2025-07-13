# Chat Snake

An experiment with Streamlit and fuzzywuzzy to see how quickly a user interface could be deployed in under 20 minutes of coding with a mostly convincing chatbot experience. This is an ultra-minimal Python chatbot using **Streamlit** for web interface and **fuzzywuzzy** for intelligent question matching, targeting **30-40 lines of code** total.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) - Python package manager
- Python 3.13 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/anvil-of-fury/chat-snake.git
   cd chat-snake
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

## Tests
    ```bash
    uv run pytest test_chatbot.py
    ```

## Usage

Run the Streamlit application:
```bash
uv run streamlit run chatbot.py
```

The application will start a local web server (typically at `http://localhost:8501`) where you can interact with the chatbot.

