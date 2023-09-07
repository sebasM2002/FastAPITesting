from fastapi import FastAPI
from langchain import example_generator
app = FastAPI()

@app.get("/")
def index():
    text = example_generator(prompt="Hola, mundo!")
    print ({"text": text})