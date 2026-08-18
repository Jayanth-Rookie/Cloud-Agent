import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI
from functions.get_file_info import get_file_info

def generate_content(client, messages, verbose=False):
    """Handles the API call to the LLM and conditionally prints metadata."""
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )

    if response.usage is None:
        raise RuntimeError("Failed to retrieve token usage metadata.")

    if verbose:
        user_prompt = messages[-1]["content"]
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    
    content = response.choices[0].message.content
    print(content)
    
    return content

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None:
        raise RuntimeError("OPENROUTER_API_KEY environment variable is not set.")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    # 4. Get file info for the current working directory
    file_info = get_file_info(".")
    print(file_info)

    # 5. Create the conversation history list
    messages = [
        {"role": "user", "content": args.user_prompt}
    ]

    # 6. Generate content, passing the verbose flag
    generate_content(client, messages, verbose=args.verbose)

if __name__ == "__main__":
    main()