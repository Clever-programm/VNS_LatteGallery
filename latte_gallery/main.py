import uvicorn

from latte_gallery.core.setup import create_app

app = create_app()


@app.get("/app")
def read_main():
    return {"message": "Hello World", "root_path": "/api"}