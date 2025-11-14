from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
app = FastAPI()
# this allows the session cookies to go backwards and forwards between the backend and frontend
app.add_middleware(SessionMiddleware, secret_key="supersecretkey")
# base_dir holds the path import to basically say
# this is the directory to whatever folder this file ur using is in
BASE_DIR = Path(__file__).resolve().parent


# this is just taking u to the login page
@app.get("/")
async def root():
    # login page holds basedir which basically means that it is going in the directory of login.html
    login_page = BASE_DIR / "login.html"
    # html content holds th elogin page but also reads that text and then puts its format in utf8
    html_content = login_page.read_text(encoding="utf-8")
    # returns the response of this
    return HTMLResponse(html_content)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/home", response_class=HTMLResponse)
async def home():
    about_path = BASE_DIR / "home.html"
    html_content = about_path.read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)

# this one dont require a passowrd
@app.get("/about", response_class=HTMLResponse)
async def about():
    about_path = BASE_DIR / "about.html"
    html_content = about_path.read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)

@app.post("/login")
async def login(request: Request):
    body = await request.json()
    # this goes into the body of the username and finds where it says username,
    # then stores it in this variable
    username = body.get("username")
    # this does the same as the username above, but it stores the password it finds
    password = body.get("password")

    if username == "Stuart" and password == "Pot":
        # this is saving the user on the client side, so it's saving the data on
        # the computer its running on, not the cloud. we can refer to the username as user now.
        # a session will allow them to store all of it
        request.session["user"] = username
        return JSONResponse({"message": "Login successful! Welcome, Stuart."})
    else:
        return JSONResponse({"message": "Invalid username or password."}, status_code=401)

@app.post("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=303)

# this one requires password

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    # wherever the name "user" is used, it's gonna get that data and put it in this variable
    user = request.session.get("user")
    # if the user does not match what is in user
    if not user:
        # it will throw an error and not work
        return RedirectResponse(url="/", status_code=303)

    html_path = BASE_DIR / "dashboard.html"
    html_content = html_path.read_text(encoding="utf-8")

    # Replace placeholder with actual username
    html_content = html_content.replace("{{user}}", user)

    return HTMLResponse(content=html_content)

@app.get("/monkey_balls", response_class=HTMLResponse)
async def dashboard(request: Request):
    user = request.session.get("user")
    if not user:
        return RedirectResponse(url="/", status_code=303)
    html_path = BASE_DIR / "monkey_balls.html"
    html_content = html_path.read_text(encoding="utf-8")
    html_content = html_content.replace("{{user}}", user)
    return HTMLResponse(content=html_content)

@app.get("/not_so_personal", response_class=HTMLResponse)
async def casino_cups_page():
    casino_cups = BASE_DIR / "not_so_personal.html"
    html_content = casino_cups.read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)

@app.get("/personal_life", response_class=HTMLResponse)
async def about_me(request: Request):
    user = request.session.get("user")
    if not user:
        return RedirectResponse(url="/", status_code=303)
    html_path = BASE_DIR / "personal_life.html"
    html_content = html_path.read_text(encoding="utf-8")
    html_content = html_content.replace("{{user}}", user)
    return HTMLResponse(content=html_content)





