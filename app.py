from fastapi import FastAPI
from pydantic import BaseModel
from diffusers import StableDiffusionPipeline
import torch
from io import BytesIO
from fastapi.responses import StreamingResponse

app = FastAPI()

pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

class Prompt(BaseModel):
    prompt: str

@app.post("/generate")
def generate_image(data: Prompt):
    image = pipe(data.prompt).images[0]
    buf = BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")
