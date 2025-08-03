# using multipart form data : When data isn't sent as JSON

from fastapi import FastAPI, Form, File, UploadFile
from typing import Optional

app = FastAPI()


@app.post("/profile/update")
async def update_profile(
    username: str = Form(..., description="The new username"),
    profile_picture: Optional[UploadFile] =  File(None, description="A new profile picture")
):

    file_info = "No file uploaded"
    if profile_picture:
        # In a real app, one would save the file to a storage service(eg S3)
        # But now just reading its properties
        file_info = {
            "filename": profile_picture.filename,
            "content_type": profile_picture.content_type,
        }
        # file content can be read with : contents = await profile_picture.read()
    return {"username": username, "profile_picture": file_info}

## Notes : 
"""
1. Form Fields: To receive form fields, you use the Form dependency. 
username: str = Form(...) declares a required form field named username.

2. File Uploads: To receive an uploaded file, you use File and UploadFile. UploadFile is recommended as it handles large files efficiently by streaming them to disk instead of loading them entirely into memory.

3. Mixing Fields and Files: You can declare multiple Form and File parameters in a single endpoint. FastAPI understands that this requires a multipart/form-data request. Note that you cannot simultaneously receive JSON (Body) and form/file data in the same request, as this is a limitation of the HTTP protocol.

"""