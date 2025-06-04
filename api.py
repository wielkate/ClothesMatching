from fastapi import FastAPI, UploadFile, File

from process_image import process_image_with_name

app = FastAPI()


@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    color_name = process_image_with_name(file.filename)
    return {"message": "Image uploaded", "filename": file.filename, "color": color_name}
