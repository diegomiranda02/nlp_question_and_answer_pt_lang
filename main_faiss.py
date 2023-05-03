# fastapi libraries
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

# Import NLP API
from services import nlp_api

# Instantiate the API
app = FastAPI()

# Decide who can access te API
origins = [
    "http://localhost",
    "http://localhost:8501"
]

# Insert the access permissions in the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check if the API is Alive
@app.get("/", response_class=PlainTextResponse)
async def root():
    return "API is Alive"

# Return an Answer for a Question, based on the content
@app.get("/answer", response_class=PlainTextResponse)
async def answer(question: str):
    # Get the answer with 4 most similar results
    answer = nlp_api.getAnswer(question, 4)
    return answer
