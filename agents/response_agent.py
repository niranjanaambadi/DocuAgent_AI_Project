from langchain.llms import HuggingFaceHub
llm = HuggingFaceHub(repo_id="google/flan-t5-base")
def generate_response(doc_text):
  prompt = f"Summarize the key obligations and risks in the following document:\n\n{doc_text[:2000]}"
  return llm(prompt)
