from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from tasks.routes import router as tasks_routes


app = FastAPI(
    title="Simple Todo App Api",
    description="this is a simple blog app with minimal usage of authentication and post managing",
    version="0.0.1",
    terms_of_service="",
    contact={
        "name": "Omid Magi",
        "url": "https://gemini.google.com/",
        "email": "omidmaghsoudi.dm@gmail.com",
    },
    license_info={"name": "MIT"},
    docs_url= None,
)

# swagger-ui
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/docs")
async def custom_swagger_ui_html():
    return HTMLResponse("""
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <title>Swagger UI</title>
        <link href="/static/swagger-ui/swagger-ui.css" rel="stylesheet" />
        <script src="/static/swagger-ui/swagger-ui-bundle.js"></script>
      </head>
      <body>
        <div id="swagger-ui"></div>
        <script>
          const ui = SwaggerUIBundle({
            url: "/openapi.json",
            dom_id: '#swagger-ui',
          });
        </script>
      </body>
    </html>
    """)



app.include_router(tasks_routes)
