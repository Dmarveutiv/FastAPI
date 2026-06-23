from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Kilanko Daniel",
        "title": "I am super sexy",
        "content": "Daniel is a sexy boy, not just sexy but in love",
        "date_posted": "April 20, 2026",
    },
    {
        "id": 2,
        "author": "Batman",
        "title": "I am Vengeance",
        "content": "I am the night, I am Batman",
        "date_posted": "June 21, 2026",
    },
]


@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": posts, "title": "Home"},
    )


@app.get("/api/posts")
def get_posts():
    return posts