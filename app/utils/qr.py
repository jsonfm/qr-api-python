from typing import Union, List

from PIL import Image
import qrcode
from pyzbar.pyzbar import decode

# utils
from app.utils.images import base64_to_image, image_to_base64


def generate_qr(content: str, to_base64: bool = True):
    """Generates a QR image."""
    image = qrcode.make(content)
    image = image.get_image()
    if to_base64:
        image = image_to_base64(image)
    return image


def decode_qr_image(image: Union[Image.Image, str]):
    """Decodes QR image."""
    image = base64_to_image(image)
    result = decode(image)[0]
    polygon = [{"x": point.x, "y": point.y} for point in result.polygon]
    rect = result.rect
    rect = {"left": rect.left, "top": rect.top, "width": rect.width, "height": rect.height}
    data = {
        "content": result.data,
        "type": result.type,
        "rect": rect,
        "quality": result.quality,
        "polygon": polygon,
        "orientation": result.orientation
    }
    return data
