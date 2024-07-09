from pygame import Surface, Rect, Color, font
from pygame.font import Font

class TextBox:
    def __init__(tb, text: str, font: Font, location: tuple | Rect, text_color: Color = Color(0, 0, 0)) -> None:
        tb.text = text
        tb.font = font
        tb.location = location
        tb.surface = tb.font.render(tb.text, False, text_color)
        tb.active = True
        tb.show = True
    
    def set_location(tb, location: tuple | Rect) -> tuple | Rect:
        if isinstance(location, (tuple, Rect)):
            tb.location = location
        else: print("Invalid location given.")

class TextBucket:
    def __init__(tb, canvas: Surface) -> None:
        tb.canvas = canvas
        tb.fonts = {"Consolas": font.SysFont("Consolas", 18)}
        tb.text_boxes = {}

    def _create_text_box(tb, text: str, location: tuple):
        return TextBox(text, tb.fonts["Consolas"], location)

    def add(tb, id: str, text: str, location: tuple):
        try:
            tb.text_boxes[id] = tb._create_text_box(text, location)
        except Exception as E:
            print(E)
    
    def dump(tb, id: str):
        try:
            del tb.text_boxes[id]
        except:
            print("Something went wrong. Could Not Delete Text Box.")
    
    def alter_location(tb, id: str, location: tuple | Rect):
        try:
            tb.text_boxes[id].set_location(location)
        except:
            print("Something went wrong. Could Not Alter Text Box Location.")

    def update(tb):
        for index, key in enumerate(tb.text_boxes):
            text_box = tb.text_boxes[key]
            if text_box.show:
                tb.canvas.blit(text_box.surface, text_box.location)