from typing import List, Optional
from fastapi import FastAPI, Header, Response
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/headers/")
async def read_and_set_headers(
    response: Response, # Injecting the response object
    user_agent: Optional[str] = Header(None),
    x_custom_token: Optional[List[str]] = Header(None, description="Custom token, can appear multiple times")   
):
    # can set a custom header on the response
    response.headers["X-App-Version"] = "1.2.3"

    # also can return a JSONResponse directly with headers
    # Note: Returning a JSONResponse will override the headers set on the 'response' object earlier.
    content = {"User-Agent":user_agent, "X-Custom_Token-Values": x_custom_token}
    headers = {"X-Another-Header": "some-value", "Content-Language": "en-US"}

    return {"User-Agent": user_agent, "X-Custom-Token-Values": x_custom_token}