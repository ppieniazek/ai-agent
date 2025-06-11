import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    user_prompt = " ".join(args)
    if verbose:
        print("User prompt:", user_prompt)

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    generate_response(client, messages, verbose)


def generate_response(
    client: genai.Client, messages: list[types.Content], verbose: bool
):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:", response.text, sep="\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()
    else:
        print("No arguments provided!")
        sys.exit(1)
