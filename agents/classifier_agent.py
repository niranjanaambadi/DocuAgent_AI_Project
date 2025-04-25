from transformers import pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
def classify_document(text):
  labels = ["contract", "invoice", "legal notice", "financial report"]
  result = classifier(text, candidate_labels=labels)
  return result["labels"][0]
