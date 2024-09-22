from PIL import Image
import sys
import json

def get_unique_colors(image_path)->list[int]:
    # Open the image file
    img = Image.open(image_path)
    # Convert the image to RGB mode
    img = img.convert('RGB')

    # downscale to 64 colors
    img = img.quantize(colors=64)

    signed_palette = []
    palette = img.getpalette()
    for i in range(0, len(palette), 3):
        signed_int32_color = convert_color_to_ARGB_signed_int32(255, palette[i], palette[i + 1], palette[i + 2])
        signed_palette.append(signed_int32_color)

    
    return signed_palette


def convert_color_to_ARGB_signed_int32(a: int, r: int, g: int, b: int)->int:
    hex_value = '{:02x}{:02x}{:02x}{:02x}'.format(a, r, g, b)
    signed_int = int(hex_value, 16)
    if signed_int > 0x7FFFFFFF:
        signed_int = signed_int - 0x100000000
    return signed_int


def export_infinite_painter_palette(palette: list[int]):
    formatted_palette = {
        "colors": palette,
        "name": "Infinite Painter Palette"
    }
    return json.dumps(formatted_palette, indent=4)
    


if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print("Usage: python main.py image_path")
        sys.exit(1)
    image_path = sys.argv[1]
    unique_colors = get_unique_colors(image_path)
    print(export_infinite_painter_palette(unique_colors))
    