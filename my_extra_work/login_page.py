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
#     login_page = BASE_DIR / "login.html"
#     html_content = login_page.read_text(encoding="utf-8")
#     return HTMLResponse(html_content)
#
# @app.post("/login")
# async def login(request: Request):
#     body = await request.json()
#     # this goes into the body of the username and finds where it says username,
#     # then stores it in this variable
#     username = body.get("username")
#     # this does the same as the username above, but it stores the password it finds
#     password = body.get("password")
#
#     if username == "Stuart" and password == "Pot":
#         # this is saving the user on the client side, so it's saving the data on
#         # the computer its running on, not the cloud. we can refer to the username as user now.
#         # a session will allow them to store all of it
#         request.session["user"] = username
#         return JSONResponse({"message": "Login successful! Welcome, Stuart."})
#     else:
#         return JSONResponse({"message": "Invalid username or password."}, status_code=401)