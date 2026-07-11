import random
from PIL import Image, ImageDraw

class MinesImageGenerator:
    def __init__(self):
        self.grid = 5
        self.cell = 110
        self.pad = 25

    def generate(self, num: int) -> str:
        num = max(1, min(20, num))
        total = self.grid * self.grid
        selected = random.sample(range(total), num)

        w = h = self.grid * self.cell + 2 * self.pad
        img = Image.new("RGB", (w, h), (15, 23, 42))
        draw = ImageDraw.Draw(img)

        for i in range(self.grid):
            for j in range(self.grid):
                x1 = self.pad + j * self.cell
                y1 = self.pad + i * self.cell
                x2 = x1 + self.cell
                y2 = y1 + self.cell
                idx = i * self.grid + j

                # Cell background
                if idx in selected:
                    # Diamond cell
                    draw.rounded_rectangle([x1+10, y1+10, x2-10, y2-10], 
                                         radius=22, fill=(51,65,85), outline="#34d399", width=7)
                    # Simple diamond
                    cx, cy = x1 + self.cell//2, y1 + self.cell//2
                    draw.polygon([
                        (cx, cy-35), (cx+25, cy), (cx, cy+35), (cx-25, cy)
                    ], fill="#34d399")
                else:
                    # Normal cell
                    draw.rounded_rectangle([x1+10, y1+10, x2-10, y2-10], 
                                         radius=22, fill=(51,65,85), outline="#475569", width=4)

        path = f"mines_{random.randint(10000,99999)}.png"
        img.save(path, quality=95)
        return path

generator = MinesImageGenerator()
