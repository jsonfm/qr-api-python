from fastapi import FastAPI, HTTPException

# utils
from app.utils.qr import generate_qr, decode_qr_image


# schemas
from app.schemas.encode import EncodeSchema, EncodeResponse
from app.schemas.decode import DecodeSchema, DecodeResponse

# middlewares
from app.middlewares.cors import apply_cors_middleware


app = FastAPI(title="QR encoder/decoder API.", description="Generates base64 QR images and decodes base64 images as strings.")
app = apply_cors_middleware(app)


@app.post("/encode", tags=["QR"], description="Generate a QR Image.", response_model=EncodeResponse)
def encode(schema: EncodeSchema):
    """Encodes some string message as QR image."""
    try:
        content = schema.content
        result = generate_qr(content)
        response = {
            "image": result
        }
        return response
    except Exception as e:
        raise HTTPException(400, str(e))


@app.post("/decode", tags=["QR"], description="Decode a QR Image", response_model=DecodeResponse)
def decode(schema: DecodeSchema):
    """Decodes a QR Image."""
    try:
        image = schema.image
        result = decode_qr_image(image)
        return result
    except Exception as e:
        raise HTTPException(400, str(e))