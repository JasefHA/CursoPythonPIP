import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4]

#renderizar html de manera dinamica
@app.get('/contact', response_class = HTMLResponse)
def get_list():
    return """
    <h1> Curso PIP Python </h1>
    <p> Mi nombre es Jasef </p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()