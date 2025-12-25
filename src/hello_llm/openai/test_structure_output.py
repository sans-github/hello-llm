from openai import OpenAI

import tiktoken


class TestStructureOutput:
    MAX_OUTPUT_TOKENS = 30

    def __init__(self):
        # export OPENAI_API_KEY="..."
        self.client = OpenAI()

    def chat_with_llm(self, prompt):
        enc = tiktoken.encoding_for_model("gpt-5-mini-2025-08-07")
        input_token_len = len(enc.encode(prompt))
        print(f"ℹ️ input_token_len: {input_token_len}")

        input = (
            "Return ONLY valid JSON.\n"
            "No explanations. No markdown. No text outside JSON.\n\n"
            f"Extract key info and return JSON: {prompt}"
        )
        return self.client.responses.parse(
            input=input,
            model="gpt-5-mini-2025-08-07",
            max_output_tokens=self.MAX_OUTPUT_TOKENS,
            timeout=100
        )


if __name__ == "__main__":
    test_structure_output = TestStructureOutput()
    # "Hey, reach me at john@email.com or call 555-1234"
    user_input = input("You: ")
    while True:
        if user_input.lower() not in {"quit", "exit"}:
            llm_output = test_structure_output.chat_with_llm(user_input)
            print(f"llm : {llm_output}")
        else:
            break
