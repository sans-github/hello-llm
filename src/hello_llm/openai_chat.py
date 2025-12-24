from openai import OpenAI

client = OpenAI()

print(f"==client type = {type(client)}==")

# client = OpenAI(api_key="your-api-key-here")
# Instead, set as env variable
# export OPENAI_API_KEY="..."


def chat_with_gpt(prompt):
    gpt_response = client.responses.create(model="gpt-5-nano", input=prompt)
    return gpt_response.output_text


if __name__ == "__main__":
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
        response = chat_with_gpt(user_input)
        print("Response: ", response)
