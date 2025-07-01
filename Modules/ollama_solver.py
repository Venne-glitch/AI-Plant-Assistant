import ollama 

def generate_response(context, question):
    prompt = f"""You are a plant expert AI. Here is detailed information about a plant:

{context}

Now answer the following question:
{question}

Answer:"""
    response = ollama.chat(model="tinyllama", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]
