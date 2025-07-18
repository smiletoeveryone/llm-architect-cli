
import subprocess

def query_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3:latest"],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()
