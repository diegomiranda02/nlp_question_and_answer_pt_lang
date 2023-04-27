# Transformers Library
import transformers
from transformers import pipeline

# IA Model
model_name = 'pierreguillou/bert-base-cased-squad-v1.1-portuguese'
nlp = pipeline("question-answering", model=model_name)

# Call NLP method to get the answer
def getAnswer(content, question):  
    result = nlp(question=question, context=content)
    return result['answer']
