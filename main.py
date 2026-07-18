import argparse
import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from call_function import available_functions, call_function
from prompts import system_prompt


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None:
        raise RuntimeError("Api key not found in the environment.")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
    generate_content(client, messages, args.verbose)


def generate_content(
    client: OpenAI,
    messages: list,
    verbose: bool,
) -> None:
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )
    if response.usage is None:
        raise RuntimeError("Failed request")
    if verbose:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    message = response.choices[0].message
    if message.tool_calls:
        for tool_call in message.tool_calls:
            if tool_call.type != "function":
                continue
            result_message = call_function(tool_call, verbose)
            if not result_message.get("content"):
                raise RuntimeError(
                    f"Calling {tool_call.function.name} function failed."
                )
            if verbose:
                print(f"-> {result_message['content']}")
    else:
        print(f"Response:\n{message.content}")


if __name__ == "__main__":
    main()
