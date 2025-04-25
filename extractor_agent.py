from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
llm = HuggingFaceHub(repo_id="google/flan-t5-base")
clause_names = ["termination clause", "confidentiality clause", "payment terms"]
def extract_clauses(doc_text):
   template = PromptTemplate.from_template(
    "Extract the {clause} from the following text:\n\n{doc_text}"
    )
  results = {}
  for clause in clause_names:

      prompt = template.format(clause=clause, doc_text=doc_text[:1500])
      result = llm(prompt)
      results[clause] = result
  return results
