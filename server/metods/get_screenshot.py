import PIL
from PIL import Image, ImageGrab, ImageDraw
import mouse
import time
import os


def get_screenshot(num):
    currentMouseX, currentMouseY = mouse.get_position()
    img = PIL.ImageGrab.grab()
    img.save("screen.png", "png")
    img = Image.open("screen.png")
    draw = ImageDraw.Draw(img)
    draw.polygon(
        (currentMouseX, currentMouseY, currentMouseX, currentMouseY + 20, currentMouseX + 13, currentMouseY + 13),
        fill="white", outline="black")

    current_time = time.localtime()
    file_name = f"screen_{current_time.tm_mday}_{current_time.tm_mon}_{current_time.tm_hour}{current_time.tm_min}.png"
    directory = "../../client/screens"
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, file_name)
    img.save(file_path, "PNG")
    if os.path.exists("screen.png"):
        os.remove("screen.png")
    return f"Скриншот сохранен в {directory} и {num}"


