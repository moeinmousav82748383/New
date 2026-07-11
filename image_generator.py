import random
from PIL import Image, ImageDraw, ImageFont

class MinesImageGenerator:
    def __init__(self):
        self.grid = 5
        self.cell = 110
        self.pad = 20

    def generate(self, num: int) -> str:
        num = max(1, min(20, num))
        total = self.grid * self.grid
        selected = random.sample(range(total), num)

        w = h = self.grid * self.cell + 2 * self.pad
        img = Image.new("RGB", (w, h), (15, 23, 42))
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", 65)
        except:
            font = ImageFont.load_default()

        for i in range(self.grid):
            for j in range(self.grid):
                x1 = self.pad + j * self.cell
                y1 = self.pad + i * self.cell
                idx = i * self.grid + j

                if idx in selected:
                    draw.rounded_rectangle([x1+8, y1+8, x1+self.cell-8, y1+self.cell-8], 
                                         radius=20, fill=(51,65,85), outline="#22d3b3", width=6)
                    draw.text((x1+self.cell//2-25, y1+self.cell//2-35), "💎", fill="#34d399", font=font)
                else:
                    draw.rounded_rectangle([x1+8, y1+8, x1+self.cell-8, y1+self.cell-8], 
                                         radius=20, fill=(51,65,85), outline="#475569", width=4)

        path = f"mines_{random.randint(1000,9999)}.png"
        img.save(path)
        return path

generator = MinesImageGenerator()