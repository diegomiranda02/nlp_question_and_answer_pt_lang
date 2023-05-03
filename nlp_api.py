# Import 
import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

#Data
data = [['Quais as centrais que estarão fazendo o cadastramento?', 'As centrais de João Câmara e São Paulo do Potengi'],
['Quando vai começar a biometria?', 'Quinta-feira, 27 de abril de 2023.'],
['Qual o número do provimento', '12345'],
['Prazo para fazer o cadastramento', '30 dias'],
['Formulário de Devolução de Diárias', 'https://portal.tre-rn.jus.br/intranet/portal/formularios'],
['Máquina com maior número de vulnerabilidades nos últimos 30 dias', 'Máquina teste']]
df = pd.DataFrame(data, columns = ['question', 'answer'])

# Encoding data
text = df['question']
encoder = SentenceTransformer("ricardo-filho/bert-base-portuguese-cased-nli-assin-2")
vectors = encoder.encode(text)

#Adding vectors to FAISS index
vector_dimension = vectors.shape[1]
index = faiss.IndexFlatL2(vector_dimension)
faiss.normalize_L2(vectors)
index.add(vectors)

# Call NLP method to get the answer
def getAnswer(question, k):  
    # Encoding the question
    search_vector = encoder.encode(question)
    _vector = np.array([search_vector])
    faiss.normalize_L2(_vector)

    # Getting the distances 
    distances, ann = index.search(_vector, k=k)

    # Converting the results to a Pandas Dataframe
    results = pd.DataFrame({'distances': distances[0], 'ann': ann[0]})

    # Merging the results with the original dataset
    merge = pd.merge(results, df, left_on='ann', right_index=True)

    # Getting the first result
    result = merge.iloc[0]['answer']

    return result
