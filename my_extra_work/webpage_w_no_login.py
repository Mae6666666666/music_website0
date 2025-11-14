# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# from pathlib import Path
# from fastapi.responses import JSONResponse
# from fastapi import Request
# from fastapi.responses import RedirectResponse
# from starlette.middleware.sessions import SessionMiddleware
#
# app = FastAPI()
# BASE_DIR = Path(__file__).resolve().parent
#
# @app.get("/")
# async def root():
#     not_a_login_page = BASE_DIR / "not_a_login.html"
#     html_content = not_a_login_page.read_text(encoding="utf-8")
#     return HTMLResponse(html_content)
