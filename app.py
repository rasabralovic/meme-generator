import base64
import io
import os
from flask import Flask, url_for, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        topText = request.form["top"]
        bottomText = request.form["bottom"]
        image = request.files["slika"]
        if image.filename == "":
            return render_template("index.html")
        newImage = drawPic(image, topText, bottomText)
        bafer = io.BytesIO()
        newImage.save(bafer, format="PNG")
        meme = base64.b64encode(bafer.getvalue()).decode()
        return render_template("index.html", meme=meme)
        
        
    
    return render_template("index.html")

def drawPic(image, topText, bottomText):
    slika = Image.open(image)
    slika = slika.convert("RGB")
    draw = ImageDraw.Draw(slika)

    startSize = max(20, slika.height // 10)
    maxWidth = slika.width - 30

    font, obrub = fitFont(draw, topText, maxWidth, startSize)

    okvir = draw.textbbox((0, 0), topText, font=font, stroke_width=obrub)
    sirina = okvir[2] - okvir[0]
    visina = okvir[3] - okvir[1]

    x = slika.width / 2 - sirina / 2
    y = 15
    draw.text((x, y), topText, font=font, fill="white", stroke_width=obrub, stroke_fill="black")

    font, obrub = fitFont(draw, bottomText, maxWidth, startSize)

    okvir = draw.textbbox((0, 0), bottomText, font=font, stroke_width=obrub)
    sirina = okvir[2] - okvir[0]
    visina = okvir[3] - okvir[1]

    x = slika.width / 2 - sirina / 2
    y = slika.height - visina - 70
    draw.text((x, y), bottomText, font=font, fill="white", stroke_width=obrub, stroke_fill="black")

    return slika

def fitFont(draw, text, maxWidth, startSize):
    size = startSize
    while size > 10:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", size)
        obrub = max(2, size // 15)
        okvir = draw.textbbox((0, 0), text, font=font, stroke_width=obrub)
        if okvir[2] - okvir[0] <= maxWidth:
            break
        size -= 2
    return font, obrub

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)