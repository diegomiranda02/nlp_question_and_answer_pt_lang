# fastapi libraries
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

# service created to abstract the nlp_ai library functionalities
from services import nlp_ai

# Instantiate the API
app = FastAPI()

# Decide who can access te API
origins = [
    "http://localhost",
    "http://localhost:8501",
    "https://8501-giuferreira-cursotecnic-cew0gqba5so.ws-us92.gitpod.io", # Substitua pela url da sua aplicacao Streamlit (No gitpod está na aba Ports)
]

# Insert the access permissions in the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# function to return the content
def getContent(): 
    content = "A segunda etapa do retorno da coleta dos dados biométricos foi iniciada nos seguintes municípios: Parnamirim (50ª ZE), Macaíba (5ª ZE), São Gonçalo do Amarante (51ª), Ceará Mirim (6ª e 46ª ZE’s), Extremoz (64ª ZE) e Touros (14ª). Além dos cartórios eleitorais de cada Zona, as Centrais de atendimento da Justiça Eleitoral em Ceará-Mirim, São Gonçalo do Amarante, Parnamirim e Macaíba também estarão realizando a coleta."
    content += "Os eleitores que efetuarem Requerimento de Alistamento Eleitoral (alistamento, transferência ou revisão) através do Título Net, terão o prazo de 30 dias para realizarem a coleta biométrica. O cadastramento é destinado também aos eleitores que fizeram alistamento, transferência ou revisão durante o período da pandemia e não coletaram os seus dados biométricos."
    content += "Para fazer a coleta não é necessário agendamento prévio, basta a(o) eleitora(o) dirigir-se ao seu cartório eleitoral ou Centrais, das 8h às 13h, portando o seu documento oficial com foto e comprovante de residência."
    content += "A partir desta quinta-feira (27) o cadastramento biométrico será iniciado em mais seis Zonas Eleitorais, seguindo o cronograma do retorno gradual do procedimento. Serão contemplados os seguintes municípios: João Câmara (10ª e 62ª ZE’s), São Bento do Norte (52ª ZE), São Paulo do Potengi (8ª ZE), São Tomé (19ª ZE), São José do Campestre (15ª ZE) e Tangará (53ª ZE). As Centrais de atendimento em João Câmara e São Paulo do Potengi também estarão fazendo o cadastramento."
    content += "As datas de retomada nos demais municípios do Estado serão anunciadas a partir da proximidade da reabertura do cadastramento nesses locais. A retomada gradual do cadastramento de dados biométricos no atendimento das eleitoras e dos eleitores do Rio Grande do Norte está prevista no Provimento nº 1/2023 da Corregedoria Regional Eleitoral (CRE)."
    content += "O Tribunal Regional Eleitoral do Rio Grande do Norte (TRE-RN) reforça que o eleitor que ainda não coletou sua biometria, vai ter acesso ao serviço até o fechamento do cadastro, que só deve ocorrer um pouco antes das eleições municipais de 2024."

    return content

# Check if the API is Alive
@app.get("/", response_class=PlainTextResponse)
async def root():
    return "API is Alive"

# Return an Answer for a Question, based on the content
@app.get("/answer", response_class=PlainTextResponse)
async def answer(question: str):
    content = getContent()
    answer = nlp_ai.getAnswer(content, question)
    return answer


