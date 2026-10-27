from PIL import Image, ImageDraw
from pathlib import Path
from fractales.art.flower import draw_flower

SIZE=800
SCALE = 3

def create_canvas(size, supersamble=3, background = (5,7,19)):
    real_size = size * supersamble
    image = Image.new("RGB",(real_size,real_size),background)
    return image

def to_final_resolution(image,size):
    return image.resize((size,size),Image.Resampling.LANCZOS)

if __name__ == "__main__":
    image=create_canvas(SIZE)
    draw = ImageDraw.Draw(image)

    center = (SIZE*SCALE // 2, SIZE*SCALE//2)

    draw_flower(draw,center,petals=12,radius=400*SCALE,width=45*SCALE, rotation=0.0,color=(180,130,255))

    image = to_final_resolution(image,SIZE)
    Path("outputs").mkdir(parents=True,exist_ok=True)
    image.save("Outputs/flower.png")
