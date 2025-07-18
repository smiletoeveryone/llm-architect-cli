import readline
import time
from ollama_interface import query_ollama

def typewriter_print(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to next line after completion

def run_cli():
    print("🔧 LLaMA 3.3 Ubuntu Terminal – LLM Architect CLI\nType 'exit' to quit.")
    while True:
        try:
            user_input = input("🧠 > ")
            if user_input.lower() in ['exit', 'quit']:
                break
            response = query_ollama(user_input)
            typewriter_print(response)
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    run_cli()
