from openai import OpenAI
import os


class TestChat:
    def __init__(self):
        """
        # client = OpenAI(api_key="your-api-key-here") <br/>
        # Instead, set as env variable<br/>
        # export OPENAI_API_KEY="..."
        """
        self.client = OpenAI()
        print(f"==client type = {type(self.client)}==")

    def chat_with_gpt(self, prompt):
        gpt_response = self.client.responses.create(model="gpt-5-nano", input=prompt)
        return gpt_response.output_text


if __name__ == "__main__":
    os.system("clear")
    print("===Here===")
    test_chat = TestChat()
    while True:
        user_input = input("You: ")
        if user_input.lower() in [
            "quit",
            "exit",
            "close",
            "stop",
            "end",
            "terminate",
            "abort",
            "shutdown",
            "disconnect",
            "logout",
            "log out",
            "sign out",
            "leave",
            "return",
            "bye",
            "goodbye",
            "see you",
            "see ya",
            "later",
            "quit program",
            "end program",
            "close program",
            "shut down",
            "shut off",
            "finish",
            "end session",
            "cancel",
        ]:
            break
        response = test_chat.chat_with_gpt(user_input)
        print("Response: ", response)
