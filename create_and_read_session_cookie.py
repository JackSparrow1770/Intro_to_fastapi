from fastapi import FastAPI
from fastapi import Cookie, Response
from typing import Optional


app = FastAPI()

@app.get("/session/create")
def create_session_cookie(response: Response):
    response.set_cookie(
        key="session_id",
        value="fake-session-token-123",
        httponly=True, # Makes the cookie inaccessible to client-side Javascript
        secure=True,   # Ensures the cookie is only sent over HTTPS       
        samesite="lax", # Provides some CSRF protection
    )
    return {"message": "Session cookie created"}


@app.get("/session/read")
def read_session_cookie(session_id: Optional[str] = Cookie(None)):
    if not session_id:
        return {"message": "No session cookie found"}
    return {"session_id": session_id}
