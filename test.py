from PIL import Image, ImageDraw, ImageFont
import io
from requests import get
from random import choice
wrds = ["1","0", "0", "1", "0", "0", "0", "1", "0" "0", "1", "0", "1", "1", "0"]
text = "\n".join(["".join([str(choice (wrds)) for _ in range(100)]) for _ in range(100)])
font = get("https://x0.at/MHH.ttf")
font = io.BytesIO(font.content)
font = ImageFont.truetype(font, int(' '.join(message.message.split()[2::])))
temp = Image.new("L", (1, 1))
temp = ImageDraw.Draw(temp)
w, h = temp.multiline_textsize(font=font, text=text, spacing=0)
img = Image.new("RGB", (w, h), "#000")
draw = ImageDraw.Draw(img)
draw.multiline_text(xy=(0,0), text=text, font=font, fill="#fff", spacing=0)
_ = Image.open(io.BytesIO(await reply.download_media(bytes)))
im = Image.new("RGB", _.size, "#000")
im.paste(_, (0, 0), _ if _.mode=="RGBA" else None)
img = img.crop((0, 0, *im.size))
w, h = im.size
for x in range (w):
 for y in range (h):
  pix = img.getpixel((x, y))
  if pix == (0,0,0):
   im.putpixel((x, y), (0, 0, 0))
   
out = io.BytesIO()
out.name = "101.png"
im.save(out)
out.seek(0)
await reply.reply(file=out)
await message.delete()