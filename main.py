import os
import sys

from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=" ".join(sys.argv[1:]),
    )

    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:", response.text, sep="\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()
    else:
        print("No arguments provided!")
        sys.exit(1)
