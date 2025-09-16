import subprocess

def ask_ollama(question, context):
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode("utf-8")
