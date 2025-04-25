from agents.classifier_agent import classify_document
from agents.extractor_agent import extract_clauses
from agents.response_agent import generate_response
def main():
  doc_path = "data/sample_docs/contract1.txt"
  print("Reading document...")
  with open(doc_path, "r") as f:
  doc_text = f.read()
  print("\n[1] Classifying Document...")
  category = classify_document(doc_text)
  print(f"Category: {category}")
  print("\n[2] Extracting Key Clauses...")
  clauses = extract_clauses(doc_text)
  for name, clause in clauses.items():
    print(f"\n{name.upper()}:\n{clause}")
    print("\n[3] Generating Response...")
  summary = generate_response(doc_text)
  print(f"\nSuggested Summary:\n{summary}")

if __name__ == "__main__":
main()
