# Reference
* [Why Python Developers Are Switching to UV by Dave Ebbelaar](https://www.youtube.com/watch?v=5rTwOt9Qgik)
* [Create a Python GPT Chatbot - In Under 4 Minutes by Tech With Tim](https://www.youtube.com/watch?v=q5HiD5PNuck)

# Set up
1. Create a new project

    ```bash
    uv init hello-llm
    cd hello-llm
    ```

    Folder structure: `tree -a -I '.git'`
    ```txt
    ├── .gitignore
    ├── .python-version
    ├── main.py
    ├── pyproject.toml
    └── README.md
    ```
Note: I renamed `main.py` → `openai-chat.py`

2. Add dependencies: `uv add openai`
    
    Note: This also creates the virutal env `.venv`

3. Run: `uv run openai-chat.py`

# pip equivalent commands
* `pip freeze` → `uv pip freeze`