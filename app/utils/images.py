from typing import List, Union
import base64
from PIL import Image, PngImagePlugin
from io import BytesIO


def image_to_base64(
    image: Union[str, Image.Image],
    _format: str = "jpeg",
    myme: bool = True,
    fixed_rgba: bool = True
) -> str:
    """Returns a base64 string from a PIL Image."""
    if isinstance(image, str):
        return image

    if fixed_rgba:
        if image.mode == "RGBA":
            image = image.convert("RGB")

    buffer = BytesIO()
    image.save(buffer, format=_format)
    buffer.seek(0)
    encoded_image = base64.b64encode(buffer.getvalue()).decode("utf-8")

    if myme:
        myme_type = f"data:image/{_format};base64,"
        encoded_image = f"{myme_type}{encoded_image}"

    return encoded_image


def base64_to_image(image: Union[str, Image.Image]) -> Image.Image:
    """Returns a PIL image as a base64 encoded string."""
    if isinstance(image, Image.Image):
        return image

    if ";base64," in image:
        split = image.split(";base64")
        # mime_type = split[0]
        image = split[1]

    image_bytes = base64.b64decode(image)
    buffer = BytesIO(image_bytes)
    image = Image.open(buffer)
    return image